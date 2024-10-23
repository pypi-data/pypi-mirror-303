import enum

import pydantic


class FileType(enum.Enum):
    Csv = "Csv"
    Parquet = "Parquet"


class DatasetConfig(pydantic.BaseModel):
    name: str
    description: str

    def dict(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
        }
