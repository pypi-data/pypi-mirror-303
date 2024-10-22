import logging
from datetime import datetime, timedelta, timezone

import grpc

from conveyor.pb.application_runs_pb2 import (
    ApplicationRun,
    GetApplicationRunRequest,
    Phase,
)
from conveyor.pb.application_runs_pb2_grpc import ApplicationRunsServiceStub
from conveyor.pb.datafy_pb2 import CancelApplicationRequest
from conveyor.pb.datafy_pb2_grpc import EnvironmentServiceStub

from .task_runner import ApplicationRunResult, TaskState

logger = logging.getLogger(__name__)


class ContainerTaskState(TaskState):

    def __init__(
        self,
        application_run_id: str,
        container_app_name: str,
        environment_id: str,
        project_id: str,
    ):
        self.application_run_id = application_run_id
        self.container_app_name = container_app_name
        self.environment_id = environment_id
        self.project_id = project_id
        self.created = datetime.now(timezone.utc)

    def get_application_run(self, channel: grpc.Channel) -> ApplicationRun:
        service = ApplicationRunsServiceStub(channel)
        return service.GetApplicationRunByApplicationId(
            GetApplicationRunRequest(application_id=self.application_run_id)
        )

    def has_finished(self, channel: grpc.Channel) -> bool:
        logger.debug(f"Checking if job with id: {self.application_run_id} has finished")
        try:
            app_run = self.get_application_run(channel)
        except grpc.RpcError as rpc_error:
            if rpc_error.code() == grpc.StatusCode.NOT_FOUND:
                if self.created + timedelta(seconds=60) < datetime.now(timezone.utc):
                    raise Exception("The job was not found after 1 minute")
                logger.debug(f"Job not found, we assume it has not started yet")
                return False
            raise rpc_error

        return self._is_finished_state(app_run)

    def has_failed(self, channel: grpc.Channel) -> bool:
        app_run = self.get_application_run(channel)
        return self._is_failed_state(app_run)

    def cancel(self, channel: grpc.Channel) -> bool:
        environment_service = EnvironmentServiceStub(channel)
        environment_service.CancelApplication(
            CancelApplicationRequest(
                environment_id=self.environment_id,
                container_app_id=self.container_app_name,
            )
        )
        return self.get_application_run(channel).phase == Phase.Failed

    def get_application_run_result(self, channel: grpc.Channel) -> ApplicationRunResult:
        return ApplicationRunResult(
            failed=self.has_failed(channel),
            environment_id=self.environment_id,
            project_id=self.project_id,
            application_run_id=self.application_run_id,
        )
