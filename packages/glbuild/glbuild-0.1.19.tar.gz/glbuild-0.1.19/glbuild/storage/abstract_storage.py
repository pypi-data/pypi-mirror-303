"""Abstract Storage for build data."""

from abc import ABC


class AbstractStorage(ABC):
    """Abstract Storage Class."""

    def ensure_storage_available(self):
        """Ensure data storage repository exists."""
        raise NotImplementedError("This method should be override in concrete class.")

    def logs_exists(self, project_id: int, job_id: int) -> bool:
        """Returns if logs data exists for the job `job_id` in project `project_id`."""
        raise NotImplementedError("This method should be override in concrete class.")

    def save_logs(self, project_id: int, job_id: int, logs: str):
        """Save logs data for the job `job_id` in project `project_id`."""
        raise NotImplementedError("This method should be override in concrete class.")

    def count_and_last_id(self, project_id: int) -> tuple[int, int]:
        """Returns total jobs count and last collected job ID for project `project_id`."""
        raise NotImplementedError("This method should be override in concrete class.")

    def save_jobs(self, project_id: int, jobs: list[dict]) -> int:
        """Save newly collected jobs for project `project_id` and return count of new jobs."""
        raise NotImplementedError("This method should be override in concrete class.")
