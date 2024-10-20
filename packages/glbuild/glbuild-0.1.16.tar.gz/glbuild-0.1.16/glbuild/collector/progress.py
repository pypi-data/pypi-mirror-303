"""Class to manage the progression of projects data collection."""

import tempfile
import pandas as pd


class Progress:
    """Progress Class."""

    def __init__(self, projects: list[int]) -> None:
        """Constructor."""
        self.projects: list[int] = projects
        self.progress_file = tempfile.NamedTemporaryFile(delete=False)  # noqa

        # initialize progess file
        df = pd.DataFrame()
        df["project"] = projects
        df["processed"] = [False for _ in range(len(projects))]
        df.to_csv(self.progress_file.name, index=False)

    def load_unprocessed(self):
        """Get projects remaining to process."""
        df = pd.read_csv(self.progress_file.name)
        return df[~df["processed"]]["project"].to_list()

    def set_processed(self, project_id: int | str):
        """Label project as processed."""
        df = pd.read_csv(self.progress_file.name)
        df.set_index("project", inplace=True)
        df.at[project_id, "processed"] = True
        df = df.reset_index()
        df.to_csv(self.progress_file.name, index=False)
