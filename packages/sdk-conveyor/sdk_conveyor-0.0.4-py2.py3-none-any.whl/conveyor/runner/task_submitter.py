import logging
import signal
import time
from collections.abc import Iterable, Iterator
from functools import partial

from conveyor import grpc

from .container_task_runner import CancelledException
from .task_runner import ApplicationRunResult, TaskRunner, TaskState

logger = logging.getLogger(__name__)


class TaskSubmitter:

    def __init__(self, *tasks: TaskRunner):
        self.tasks = tasks

    @classmethod
    def from_list(cls, tasks: Iterable[TaskRunner]):
        return cls(*tasks)

    def run(self) -> Iterator[ApplicationRunResult]:
        with grpc.connect() as channel:
            try:
                task_states: list[TaskState] = []
                for task in self.tasks:
                    task_states.append(task.start_run(channel))
                signal.signal(
                    signal.SIGINT,
                    partial(self.handle_interrupt_manual_runs, channel, task_states),
                )

                while task_states:
                    running_task_states: list[TaskState] = []
                    for state in task_states:
                        if state.has_finished(channel):
                            yield state.get_application_run_result(channel)
                        else:
                            running_task_states.append(state)
                    if running_task_states:
                        time.sleep(10)
                    task_states = running_task_states
                return
            except CancelledException:
                return

    @staticmethod
    def handle_interrupt_manual_runs(
        channel, task_states: Iterable[TaskState], sig, frame
    ):
        logger.debug(f"Received interrupt, cancelling all running applications")
        for task_state in task_states:
            task_state.cancel(channel)
        raise CancelledException()
