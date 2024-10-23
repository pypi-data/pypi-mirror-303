from uuid import UUID, uuid4

import pydantic


class Workflow(pydantic.BaseModel):
    id: UUID = uuid4()
    name: str
    description: str
    workflow_config: dict


class WorkflowConfigVersionRead(pydantic.BaseModel):
    id: UUID = uuid4()
    workflow_id: UUID
    config: dict
    created_at: str


class WorkflowRead(pydantic.BaseModel):
    id: str
    name: str
    description: str
    organisation_id: str
    current_config_version_id: str

    workflow_config_versions: list[WorkflowConfigVersionRead]
    current_config_version: WorkflowConfigVersionRead
