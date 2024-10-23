import pydantic


class Secret(pydantic.BaseModel):
    id: str
    name: str
    secret_reference: str
    organisation_id: str
    description: str
    secret_type: str
    created_at: str
    updated_at: str
