import time
import typing

from truestate.client import get_client
from truestate.jobs.job import Job


class Workflow:
    
    def __init__(
        self,
        name: str = None,
        description: str = None,
        jobs: typing.List[Job] = None,
    ) -> None:
        if name is None:
            raise ValueError("Please define a name for your workflow")
        else:
            self.name = name

        if description is None:
            # default to an empty string
            description = ""

        self.name = name
        self.description = description
        self.jobs = jobs

        self.client = get_client()

    def sync(self):
        workflow = self.client.workflows.create_workflow(self)

        print(f"Successfully synced workflow: {self.name}")

        return workflow

    def run(self):

        workflow = self.sync()

        # wait for the DB to update...
        time.sleep(1)

        workflow_id = str(workflow['id'])
        version_id = str(workflow['current_config_version_id'])

        return self.client.workflows.run(
            workflow_id=workflow_id,
            version_id=version_id
        )

    def dict(self):
        workflow_dict = {
            "name": self.name,
            "description": self.description,
            "workflow_config": {
                "organisation_id": self.client.organisation_id,
                "jobs": [job.config() for job in self.jobs],
            },
        }

        self._validate_workflow(workflow_dict)

        return workflow_dict

    def _validate_workflow(self, workflow_dict: dict) -> None:
        # assert no duplicate job names
        job_names = [job["name"] for job in workflow_dict["workflow_config"]["jobs"]]
        duplicate_job_names = list(
            set([x for x in job_names if job_names.count(x) > 1])
        )

        if duplicate_job_names:
            raise ValueError(
                f"Duplicate job names found in workflow: {duplicate_job_names}"
            )
