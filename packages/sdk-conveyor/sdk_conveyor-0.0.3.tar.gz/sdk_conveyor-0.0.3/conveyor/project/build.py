import json
import logging
import subprocess

from conveyor.auth import validate_cli_version

logger = logging.getLogger(__name__)


class ProjectBuilder:
    def __init__(self, *, project_path: str):
        self._project_path = project_path

    def build(self) -> str:
        validate_cli_version()
        proc = subprocess.run(
            ("conveyor", "build", "-ojson"),
            stdout=subprocess.PIPE,
            text=True,
            cwd=self._project_path,
        )
        if proc.returncode == 0:
            build_id = json.loads(proc.stdout)["id"]
            logger.info(f"Build successful with id: {build_id}")
            return build_id
        else:
            raise Exception("The build failed")
