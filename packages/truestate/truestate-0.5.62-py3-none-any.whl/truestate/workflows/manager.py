import typing
import uuid

from truestate.workflows.models import WorkflowRead, WorkflowConfigVersionRead
from truestate.exceptions import APIError

if typing.TYPE_CHECKING:
    from truestate.client import Client
    from truestate.workflows.workflow import Workflow


class WorkflowManager:

    def __init__(self, client: 'Client') -> None:
        self.client = client

    def create_workflow(self, workflow: 'Workflow') -> WorkflowRead:
        status_code, result = self.client.post("/workflows/", data=workflow.dict())

        if status_code == 422:
            raise Exception(f"Invalid workflow configuration: {result}")

        elif status_code == 200:
            return WorkflowRead.model_validate(result)

        elif status_code == 409:
            # get the workflow first

            status_code, existing_workflow = self.client.get(
                f"/workflows/?name={workflow.name}"
            )

            if len(existing_workflow) == 0:
                raise Exception("Workflow not found")

            existing_workflow_id = existing_workflow[0]["id"]
            existing_workflow_desc = existing_workflow[0]["description"]

            if workflow.description != existing_workflow_desc:
                self.update_workflow(existing_workflow_id, workflow)

            status_code, result = self.create_workflow_config(
                id=existing_workflow_id, workflow=workflow
            )

            updated_config = WorkflowConfigVersionRead(**result)

            return WorkflowRead(
                id=existing_workflow_id,
                name=workflow.name,
                description=workflow.description,
                organisation_id=self.client.organisation_id,
                current_config_version_id=str(updated_config.id),
                workflow_config_versions=[updated_config],
                current_config_version=updated_config,
            ).model_dump()

        else:
            raise APIError(f"Failed to create workflow: {result}")

    def update_workflow(self, id: str, workflow):
        status_code, result = self.client.patch(
            f"/workflows/{id}",
            data={
                "name": workflow.name,
                "description": workflow.description,
            },
        )

        return status_code, result

    def create_workflow_config(self, id: str, workflow):
        
        body = {
            "organisation_id": self.client.organisation_id,
            "jobs": [job.config() for job in workflow.jobs],
        }

        status_code, result = self.client.post(f"/workflows/{id}/versions/", data=body)

        return status_code, result

    def get(self, workflow_id: uuid.UUID = None, name: str = None):
        if workflow_id and name:
            raise Exception("Only one of workflow_id or name can be provided")

        if name:
            status_code, result = self.client.get(f"/workflows/?name={name}")
            return result

        elif workflow_id:
            status_code, result = self.client.get(f"/workflows/{workflow_id}/")
            return result

        else:
            status_code, result = self.client.get(f"/workflows/")
            return result

    def run(self, workflow_id: str, version_id: str):
        status_code, response = self.client.post(
            f"/workflows/{workflow_id}/runs/",
            data={"workflow_config_version_id": version_id},
        )

        return response

    def delete(self, workflow_id: uuid.UUID):
        status_code, response = self.client.delete(
            f"/workflows/{workflow_id}",
        )
        assert status_code == 200

        return response

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        return self.get()
