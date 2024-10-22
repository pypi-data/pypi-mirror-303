from abc import ABC, abstractmethod

import grpc

from conveyor.auth import get_api_url
from conveyor.pb.application_runs_pb2 import ApplicationRun, Phase


class CancelledException(BaseException):
    """Cancelled the logs."""


class ApplicationRunResult:
    def __init__(
        self,
        *,
        failed: bool,
        environment_id: str,
        project_id: str,
        application_run_id: str,
    ):
        self.failed = failed
        self.environment_id = environment_id
        self.project_id = project_id
        self.application_run_id = application_run_id

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return self

    def has_failed(self) -> bool:
        return self.failed

    def conveyor_url(self) -> str:
        return f"{get_api_url()}/projects/{self.project_id}/environments/{self.environment_id}/apprun/{self.application_run_id}/logs/default"


class TaskState(ABC):

    @abstractmethod
    def has_finished(self, channel: grpc.Channel) -> bool:
        raise NotImplementedError

    @abstractmethod
    def has_failed(self, channel: grpc.Channel) -> bool:
        raise NotImplementedError

    @abstractmethod
    def cancel(self, channel: grpc.Channel) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_application_run_result(self, channel: grpc.Channel) -> ApplicationRunResult:
        raise NotImplementedError

    @staticmethod
    def _is_finished_state(app_run: ApplicationRun) -> bool:
        return (
            app_run.phase == Phase.Succeeded
            or app_run.phase == Phase.Canceled
            or app_run.phase == Phase.Failed
        )

    @staticmethod
    def _is_failed_state(app_run: ApplicationRun) -> bool:
        return app_run.phase == Phase.Failed or app_run.phase == Phase.Canceled


class TaskRunner(ABC):

    @abstractmethod
    def start_run(self, channel: grpc.Channel) -> TaskState:
        raise NotImplementedError
