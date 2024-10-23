import pydantic


class ModelConfig(pydantic.BaseModel):
    name: str
    description: str
