"""Main Class for GitLab Builds data collection"""

import math
import time
import json
import gitlab
import logging
import requests
from tqdm import tqdm
from typing import Any, Optional

from glbuild import constants
from glbuild.storage.abstract_storage import AbstractStorage
from glbuild.storage.local_storage import LocalStorage
from glbuild.collector import progress
from requests.exceptions import ChunkedEncodingError
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)  # type: ignore


logging.basicConfig(level=logging.INFO)


class GitLabBuild:
    """GitLabBuild Class."""

    def __init__(
        self,
        token: str,
        projects: list[int],
        base_url: str = constants.GITLAB_BASE_URL,
        api_version: int = 4,
        ssl_verify: bool = False,
        output: str = "./data",
        storage: Optional[AbstractStorage] = None,
        only_failure_logs: bool = True,
    ) -> None:
        """Constructor.

        Params
        ------
            projects (list[int]|int): Single of List of projects ID.
            base_url (str): GitLab instance base URL. Defaults to https://gitlab.com
            token (str): GitLab Personal Access Token.
            output (str | None): Data directory output path for LocalStorage. Defaults to `./data/`. Ignored if a custom storage is specified.
            storage (AbstractStorage | None): Custom Storage implementation. Uses LocalStorage with output as base directory if None.
        """
        self.logger = logging.getLogger(__name__)
        self.base_url: str = base_url
        self.token: str = token
        self.api_version: int = api_version
        self.ssl_verify: bool = ssl_verify
        self.projects = projects
        self.gl = gitlab.Gitlab(
            url=base_url,
            private_token=token,
            api_version=api_version,
            ssl_verify=ssl_verify,
        )
        self.progress = progress.Progress(projects=projects)
        self.storage = storage or LocalStorage(base_dir=output, projects=projects)
        self.only_failure_logs = only_failure_logs

    def start(self, n_last: Optional[int] = None, refresh: bool = True) -> bool:
        """Get historical build jobs metadata and logs from projects into path.

        Params
        ------
            n_last (int | None): Get only n last jobs. If `None`, attempts to collect all data. Defaults to `None`.
            refresh (bool): Whether to refresh data by collecting newly available data. Defaults to `True`.

        Returns
        -------
            (bool): Whether data collection was successfully completed or not.
        """
        try:
            self.gl.auth()
        except gitlab.exceptions.GitlabAuthenticationError as error:
            self.logger.error("Authentication to GitLab failed: %s", error)
            return False

        self.storage.ensure_storage_available()

        for project_id in self.progress.load_unprocessed():
            self.__collect_project_data(project_id, n_last=n_last, refresh=refresh)
            self.progress.set_processed(project_id)
            time.sleep(1)

        self.logger.info("Data collection complete sucessfully :)")
        return True

    ###################################
    #         Project Methods         #
    ###################################

    def __collect_project_data(
        self,
        project_id: int,
        n_last: Optional[int] = None,
        refresh: bool = True,
    ):
        """Collect and save jobs metadata and logs for a GitLab project.

        project_id (int): ID of the project.
        n_last (None|int): Get only n last jobs.
        """
        self.logger.info("Starting data collection for project %s...", project_id)

        old_count, last_id = self.storage.count_and_last_id(project_id)

        if old_count == 0:
            # read entire job history records
            self.logger.info("No existing data found")
            self.__collect_job_history(project_id, n_last)
        else:
            self.logger.info(
                "%s already collected jobs. Refreshing...", old_count
            )  # noqa
            if not refresh:
                return
            # else collect only new records efficiently
            count_new = 0
            for c in tqdm(self.__refresh_job_history(project_id, last_id), ncols=120):
                count_new += c
            self.logger.info("%s additionnal jobs collected", count_new)

    ###################################
    #           Job Methods           #
    ###################################

    def __refresh_job_history(self, project_id, last_id: int):
        """Collect new data up to `last_id`."""
        page: int = 0
        latest_jobs: list[dict] = []
        while last_id not in [j["id"] for j in latest_jobs]:
            page = page + 1
            count, next_jobs = self.__collect_jobs_and_logs(project_id, page=page)
            latest_jobs.extend(next_jobs)
            yield count

    def __collect_job_history(self, project_id, n_last: Optional[int]):
        """Get list of all jobs for a project using python-gitlab limited at `last`."""
        # TODO: For LocalStorage JSON always use max last at 25000
        if n_last is None:
            self.logger.info("Attempting to collect entire job history...")
            self.__collect_jobs_and_logs(project_id, all=True)
            return

        nb_pages = math.ceil(n_last / constants.JOBS_PER_PAGE)
        self.logger.info("Collecting %s jobs over %s pages", n_last, nb_pages)

        progress_bar = tqdm(range(1, nb_pages + 1), ncols=120)
        for page in progress_bar:
            self.__collect_jobs_and_logs(project_id=project_id, page=page)
        progress_bar.close()

    def __collect_jobs_and_logs(
        self,
        project_id: int,
        page: int = 1,
        per_page: int = constants.JOBS_PER_PAGE,
        all: bool = False,
    ) -> tuple[int, list[dict]]:
        """Collect and save jobs and logs on a given page for a project using python-gitlab.

        Returns count of new jobs saved and list of jobs collected.
        """
        project = self.gl.projects.get(int(project_id), lazy=True)
        params: dict[str, Any] = {
            "retry_transient_errors": True,
        }
        if all is True:
            params["all"] = True
        else:
            params["page"] = page
            params["per_page"] = per_page

        jobs = [json.loads(job.to_json()) for job in project.jobs.list(**params)]
        count = self.storage.save_jobs(project_id, jobs)
        self.__collect_logs(project_id, jobs)
        return count, jobs

    def __collect_logs(self, project_id: int, jobs: list[dict]):
        """Collect and save jobs logs."""
        # download the logs
        for job in jobs:
            if self.only_failure_logs:
                if job["status"] != "failed":
                    continue
            job_id = job["id"]
            if self.storage.logs_exists(project_id, job_id):
                continue
            # else get and save logs
            logs = self.__retrieve_job_logs(project_id, job_id)
            if logs is not None:
                self.storage.save_logs(project_id, job_id, logs)

    def __retrieve_job_logs(
        self, project_id: str | int, job_id: str | int
    ) -> Optional[str]:
        """Get job textual log data from API.

        Returns
        -------
            (str | None): Log data textual content. None if no logs available (e.g., for canceled jobs).
        """
        headers = {
            "PRIVATE-TOKEN": self.token,
        }
        url = f"{self.base_url}/api/v4/projects/{project_id}/jobs/{job_id}/trace"
        try:
            response = requests.get(
                url,
                headers=headers,
                verify=self.ssl_verify,
                timeout=constants.HTTP_REQUESTS_TIMEOUT,
            )
            return response.text
        except ChunkedEncodingError:
            # Empty log
            return None
