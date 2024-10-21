import logging
import signal
from functools import partial
from typing import List, Optional

from google.protobuf.timestamp_pb2 import Timestamp

from conveyor import grpc
from conveyor.pb.application_runs_pb2 import ScheduledBy
from conveyor.pb.common_pb2 import DatafyInstanceType, InstanceLifecycle
from conveyor.pb.datafy_pb2 import (
    CancelApplicationRequest,
    ContainerSpec,
    DatafyProjectInfo,
    ListBuildsRequest,
    ListEnvironmentsRequest,
    ListProjectsRequest,
    RunApplicationLogsRequest,
    RunApplicationRequest,
    RunApplicationResponse,
)
from conveyor.pb.datafy_pb2_grpc import EnvironmentServiceStub, ProjectServiceStub
from conveyor.project import get_project_api

from .container_task_state import ContainerTaskState
from .task_runner import ApplicationRunResult, CancelledException, TaskRunner

logger = logging.getLogger(__name__)


def copy_logs_request_with(
    req: RunApplicationLogsRequest, latest_message_timestamp: Optional[Timestamp]
) -> RunApplicationLogsRequest:
    return RunApplicationLogsRequest(
        environment_id=req.environment_id,
        environment_name=req.environment_name,
        project_id=req.project_id,
        container_app_id=req.container_app_id,
        start_from=latest_message_timestamp,
    )


class ContainerTaskRunner(TaskRunner):

    def __init__(
        self,
        *,
        task_name: str,
        project_name: str,
        environment_name: str,
        build_id: Optional[str] = None,
        command: Optional[List[str]] = None,
        args: Optional[List[str]] = None,
        instance_type: DatafyInstanceType = DatafyInstanceType.mx_micro,  # TODO can we make this InstanceType
        iam_identity: Optional[str] = None,
        instance_lifecycle: InstanceLifecycle = InstanceLifecycle.spot,
        disk_size: Optional[int] = None,
        disk_mount_path: Optional[str] = None,
        show_output: bool = True,
    ):
        self.task_name = task_name
        self.project_name = project_name
        self._project_id = None
        self.environment_name = environment_name
        self._environment_id = None
        self.build_id = build_id
        self.command = command
        self.args = args
        self.instance_type = instance_type
        self.iam_identity = iam_identity
        self.instance_lifecycle = instance_lifecycle
        self.disk_size = disk_size
        self.disk_mount_path = disk_mount_path
        self.show_output = show_output

    def project_id(self, channel: grpc.Channel):
        if self._project_id is None:
            project_service = ProjectServiceStub(channel)
            list_projects_response = project_service.ListProjects(
                ListProjectsRequest(name=self.project_name)
            )
            if not list_projects_response.projects:
                raise Exception(
                    f"No project found to match the name: {self.project_name}."
                )
            if len(list_projects_response.projects) > 1:
                raise Exception(
                    f"Multiple projects found to match the name: {self.project_name}."
                )
            self._project_id = list_projects_response.projects[0].id
        return self._project_id

    def environment_id(self, channel: grpc.Channel):
        if self._environment_id is None:
            environment_service = EnvironmentServiceStub(channel)
            list_environments_response = environment_service.ListEnvironments(
                ListEnvironmentsRequest(name=self.environment_name)
            )
            if not list_environments_response.environments:
                raise Exception(
                    f"No environment found to match the name: {self.environment_name}."
                )
            if len(list_environments_response.environments) > 1:
                raise Exception(
                    f"Multiple environments found to match the name: {self.environment_name}."
                )
            self._environment_id = list_environments_response.environments[0].id
        return self._environment_id

    def find_build_id(self, channel: grpc.Channel) -> str:
        project_service = ProjectServiceStub(channel)
        builds_response = project_service.ListBuilds(
            ListBuildsRequest(project_id=self.project_id(channel))
        )
        builds = builds_response.builds
        if len(builds) == 0:
            raise Exception("No builds found")
        else:
            return builds[0].id

    def image(self, channel: grpc.Channel, build_id: str):
        project_api = get_project_api(channel, self.project_id(channel))
        return f"{project_api.get_registry_url()}/datafy/data-plane/project/{self.project_name}:{build_id}"

    def run(self) -> ApplicationRunResult:
        with grpc.connect() as channel:
            task_state = self.start_run(channel)

            logger.debug("Fetching the logs")
            req = RunApplicationLogsRequest(
                environment_id=self.environment_id(channel),
                environment_name=self.environment_name,
                project_id=self.project_id(channel),
                container_app_id=task_state.container_app_name,
            )
            # This block makes sure we handle an interrupt while the job is running and cancel it
            # We throw and catch a cancelled exception since otherwise we would wait until the job is canceled on kubernetes
            # which by default takes up to 30s
            try:
                signal.signal(
                    signal.SIGINT,
                    partial(
                        self.handle_interrupt_manual_run,
                        channel,
                        req.environment_id,
                        req.container_app_id,
                    ),
                )
                exit_code = self.tail_logs_with_retry(channel, req)
            except CancelledException:
                return ApplicationRunResult(
                    failed=True,
                    environment_id=req.environment_id,
                    project_id=req.project_id,
                    application_run_id=task_state.application_run_id,
                )
            return ApplicationRunResult(
                failed=exit_code != 0,
                environment_id=req.environment_id,
                project_id=req.project_id,
                application_run_id=task_state.application_run_id,
            )

    def start_run(self, channel: grpc.Channel) -> ContainerTaskState:
        request = self.generate_request(channel)
        environment_service = EnvironmentServiceStub(channel)
        response: RunApplicationResponse = environment_service.RunApplication(request)
        return ContainerTaskState(
            application_run_id=response.application_run_id,
            container_app_name=response.container_app_name,
            environment_id=request.environment_id,
            project_id=request.container_spec.datafy_project_info.project_id,
        )

    def generate_request(self, channel: grpc.Channel) -> RunApplicationRequest:
        build_id = self.build_id
        if build_id is None:
            build_id = self.find_build_id(channel)

        container_spec: ContainerSpec = ContainerSpec(
            datafy_project_info=DatafyProjectInfo(
                project_id=self.project_id(channel),
                project_name=self.project_name,
                build_id=build_id,
                environment_id=self.environment_id(channel),
            ),
            image=self.image(channel, build_id),
            command=self.command,
            args=self.args,
            instance_type=DatafyInstanceType.Name(self.instance_type).replace("_", "."),
            instance_life_cycle=InstanceLifecycle.Name(self.instance_lifecycle),
            aws_role=self.iam_identity,
            azure_application_client_id=self.iam_identity,
            scheduled_by="SDK",
            disk_size=self.disk_size,
            disk_mount_path=self.disk_mount_path,
        )
        return RunApplicationRequest(
            environment_id=self.environment_id(channel),
            container_spec=container_spec,
            task_name=self.task_name,
        )

    @staticmethod
    def tail_logs_with_retry(
        channel: grpc.Channel, req: RunApplicationLogsRequest
    ) -> int:
        tries = 0
        latest_message_timestamp: Optional[Timestamp] = None
        while True:
            environment_service = EnvironmentServiceStub(channel)
            try:
                logs_response = environment_service.GetApplicationLogs(
                    copy_logs_request_with(req, latest_message_timestamp)
                )
                for log in logs_response:
                    match log.WhichOneof("response"):
                        case "log_line":
                            latest_message_timestamp = log.log_line.timestamp
                            print(log.log_line.log)
                        case "heartbeat":
                            continue
                        case "exit_code":
                            logger.debug(f"Got exit code {log.exit_code}")
                            return log.exit_code
                return 0
            except Exception as e:
                logger.debug("Got exception while tailing logs, reconnecting")
                tries += 1
                if tries >= 10:
                    logger.debug("Tries ten times, stopping")
                    raise e

    @staticmethod
    def handle_interrupt_manual_run(
        channel: grpc.Channel, environment_id: str, container_app_id: str, sig, frame
    ):
        logger.debug(
            f"Received interrupt, cancelling the application run with id {container_app_id}"
        )
        try:
            environment_service = EnvironmentServiceStub(channel)
            environment_service.CancelApplication(
                CancelApplicationRequest(
                    environment_id=environment_id, container_app_id=container_app_id
                )
            )
        except grpc.RpcError as e:
            logger.debug(f"Encountered error while cancelling the application:\n{e}")
        raise CancelledException()
