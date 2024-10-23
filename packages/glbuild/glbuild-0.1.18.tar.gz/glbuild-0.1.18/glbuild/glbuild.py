"""Main Class for GitLab Builds data collection"""

import math
import os
import time
import json
import gitlab
import logging
import requests
from tqdm import tqdm
from typing import Optional

from glbuild import constants
from glbuild.utils import utils
from glbuild.collector import progress
from requests.exceptions import ChunkedEncodingError
from urllib3.exceptions import InsecureRequestWarning


# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)  # type: ignore

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GitLabBuild:
    """GitLabBuild Class."""

    def __init__(
        self,
        token: str,
        projects: list[int],
        base_url: str = constants.GITLAB_BASE_URL,
        api_version: int = 4,
        ssl_verify: bool = False,
    ) -> None:
        """Constructor.

        Params
        ------
            projects(list[int]|int): Single of List of projects ID.
            base_url(str): GitLab instance base URL. Defaults to https://gitlab.com
            token(str): GitLab Personal Access Token.
        """
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

    def start(
        self, n: Optional[int] = None, output: str = "./data", refresh: bool = True
    ) -> bool:
        """Get historical build jobs metadata and logs from projects into path.

        Params
        ------
            n (int | None): Get only n last jobs. If `None`, tries to collect all data. Defaults to `None`.
            output (str): Directory for output. Defaults to `./data/`
            refresh (bool): Whether to refresh data by collecting any newly available data. Defaults to `True`.
        """
        # Create directories if necessary
        for path in [output, f"{output}/logs/"]:
            utils.ensure_path(path)

        for path in [f"{output}/logs/{id}" for id in self.projects]:
            utils.ensure_path(path)

        for project_id in self.progress.load_unprocessed():
            self.__get_project_data(project_id, output, last=n, refresh=refresh)
            self.progress.set_processed(project_id)
            time.sleep(1)
        return True

    ###################################
    #         Project Methods         #
    ###################################

    def __get_project_data(
        self,
        project_id: int,
        datapath: str,
        only_failures: bool = True,
        last: Optional[int] = None,
        refresh: bool = True,
    ):
        """Collect jobs metadata and logs for a GitLab project."""
        logger.info("Starting data collection for project %s...", project_id)

        # get all metadata of jobs.
        jobs = self.__get_jobs_metadata(
            project_id, datapath=datapath, last=last, refresh=refresh
        )
        logger.info("%s jobs found for collection", len(jobs))

        # download the logs
        progress_bar = tqdm(jobs, ncols=120)
        for job in progress_bar:
            if only_failures:
                if job["status"] != "failed":
                    continue

            job_log_file = f"{datapath}/logs/{project_id}/{job['id']}.log"
            # if job log file is already collected, next.
            if os.path.isfile(job_log_file):
                continue
            # else get and save logs
            logs = self.__retrieve_job_logs(project_id, job["id"])
            utils.to_file(logs, job_log_file)

        # close progress bar
        progress_bar.close()

    ###################################
    #           Job Methods           #
    ###################################

    def __get_jobs_metadata(
        self,
        project_id: int,
        datapath: str,
        last: Optional[int] = None,
        refresh: bool = True,
    ) -> list[dict]:
        """Get jobs for project (or download) and save to datapath.

        project_id(int): ID of the project.
        datapath(str): Base directory where to save the collected data.
        last (None|int): Get only n last jobs.
        """
        jobs_filepath = f"{datapath}/jobs_{project_id}.json"
        project = self.gl.projects.get(int(project_id), lazy=True)

        # read already collected json jobs
        old_jobs = utils.read_json_file(jobs_filepath) or []

        if len(old_jobs) == 0:
            # read entire job history records
            logger.info("No existing data found")
            jobs = self.__get_all_jobs(project, jobs_filepath=jobs_filepath, last=last)
        else:
            logger.info("%s jobs already collected", len(old_jobs))  # noqa
            if not refresh:
                return old_jobs

            # else read new records efficiently
            last_collected_job_id: int = max([j["id"] for j in old_jobs])  # noqa
            page: int = 1
            new_jobs = self.__get_jobs_by_page(project=project, page=page)
            # collect only new record
            while last_collected_job_id not in [j["id"] for j in new_jobs]:
                page = page + 1
                next_jobs = self.__get_jobs_by_page(project=project, page=page)
                new_jobs = utils.merge_list_dicts(
                    new_jobs, next_jobs, remove_duplicates_on="id"
                )

            jobs = utils.merge_list_dicts(old_jobs, new_jobs, remove_duplicates_on="id")
            logger.info("%s additionnal jobs found", len(jobs) - len(old_jobs))
            jobs = utils.save_json_file(jobs, jobs_filepath)
        return jobs

    def __get_and_merge_jobs_by_page(
        self,
        project,
        page: int,
        jobs_filepath: str,
        per_page: int = constants.JOBS_PER_PAGE,
    ) -> list[dict]:
        """Get list of jobs on a given page for a project using python-gitlab and merge to existing file path."""
        # TODO: Use different job file for large data collection.
        # part = (page * per_page) // 25000
        # idx = jobs_filepath[1:].index(".") + 1
        # jobs_filepath =  jobs_filepath[:idx] + f"_{part}" + jobs_filepath[idx:]
        jobs: list[dict] = utils.read_json_file(jobs_filepath) or []

        new_jobs: list[dict] = self.__get_jobs_by_page(
            project=project, page=page, per_page=per_page
        )
        if not isinstance(new_jobs, list):
            logger.warning("New collected jobs failed to be listed")
            return jobs

        jobs = utils.merge_list_dicts(jobs, new_jobs, remove_duplicates_on="id")
        jobs = utils.save_json_file(jobs, jobs_filepath)
        return jobs

    def __get_all_jobs(
        self, project, jobs_filepath: str, last: Optional[int]
    ) -> list[dict]:
        """Get list of all jobs for a project using python-gitlab."""
        if last is not None:
            last = int(last)
            nb_pages = math.ceil(last / constants.JOBS_PER_PAGE)
            logger.info("Collecting %s jobs over %s pages", last, nb_pages)
            jobs: list[dict] = []
            for page in tqdm(range(nb_pages), ncols=120):
                jobs = self.__get_and_merge_jobs_by_page(
                    project=project, page=page + 1, jobs_filepath=jobs_filepath
                )
            return jobs

        # Get all at once
        jobs = [
            json.loads(job.to_json())
            for job in project.jobs.list(all=True, retry_transient_errors=True)
        ]
        jobs = utils.save_json_file(jobs, jobs_filepath)
        return jobs

    def __get_jobs_by_page(
        self, project, page: int, per_page: int = constants.JOBS_PER_PAGE
    ) -> list[dict]:
        """Get list of jobs on a given page for a project using python-gitlab."""
        return [
            json.loads(job.to_json())
            for job in project.jobs.list(
                per_page=per_page, page=page, retry_transient_errors=True
            )
        ]

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
