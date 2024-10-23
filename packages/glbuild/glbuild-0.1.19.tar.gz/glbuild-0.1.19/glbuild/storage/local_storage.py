"""File Storage for collected build data."""

import os
import logging

from glbuild.utils import utils
from .abstract_storage import AbstractStorage


logging.basicConfig(level=logging.INFO)


class LocalStorage(AbstractStorage):
    """Local Storage Class."""

    def __init__(self, base_dir: str, projects: list[int]):
        """Local storage constructor."""
        super().__init__()
        self._logger = logging.getLogger(__name__)
        self.base_dir = base_dir
        self.projects = projects

    def ensure_storage_available(self):
        """Create data directories if not exists."""
        for path in [self.base_dir, f"{self.base_dir}/logs/"]:
            utils.ensure_path(path)
        for path in [f"{self.base_dir}/logs/{id}" for id in self.projects]:
            utils.ensure_path(path)

    def __logs_filepath(self, project_id: int, job_id: int) -> str:
        return f"{self.base_dir}/logs/{project_id}/{job_id}.log"

    def __jobs_filepath(self, project_id) -> str:
        return f"{self.base_dir}/jobs_{project_id}.json"

    def logs_exists(self, project_id: int, job_id: int) -> bool:
        """Return if logs data exists for the job `job_id` in project `project_id`."""
        return os.path.isfile(self.__logs_filepath(project_id, job_id))

    def save_logs(self, project_id: int, job_id: int, logs: str):
        """Save logs data for the job `job_id` in project `project_id`."""
        utils.to_file(logs, self.__logs_filepath(project_id, job_id))

    def read_jobs(self, project_id: int) -> list[dict]:
        """Read collected jobs for project `project_id`."""
        return utils.read_json_file(self.__jobs_filepath(project_id)) or []

    def count_and_last_id(self, project_id: int) -> tuple[int, int]:
        """Returns total jobs count and last collected job ID for project `project_id`."""
        jobs = utils.read_json_file(self.__jobs_filepath(project_id)) or []
        count = len(jobs)
        last_id = max([j["id"] for j in jobs]) if count > 0 else None  # noqa
        return count, last_id

    def save_jobs(self, project_id: int, jobs: list[dict]) -> int:
        """Save newly collected jobs for project `project_id` and return count of new jobs."""
        old_jobs = self.read_jobs(project_id)
        total_jobs = utils.merge_list_dicts(old_jobs, jobs, remove_duplicates_on="id")
        total_jobs = utils.save_json_file(total_jobs, self.__jobs_filepath(project_id))
        return len(total_jobs) - len(old_jobs)
