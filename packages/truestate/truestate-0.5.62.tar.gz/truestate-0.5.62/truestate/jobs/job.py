from abc import ABC, abstractmethod


class Job(ABC):
    def __init__(
        self, job_type: str, name: str, description: str, inputs: str, outputs: str
    ) -> None:
        self.name = name
        self.description = description
        self.job_type = job_type
        self.inputs = inputs
        self.outputs = outputs
        self.compute = None

    def __str__(self) -> str:
        return f"Job(name={self.name}, description={self.description}, job_type={self.job_type}, inputs={self.inputs}, outputs={self.outputs})"

    def config(self) -> dict:
        return {
            "name": self.name,
            "config": self.params(),
        }

    @abstractmethod
    def params(self) -> dict:
        raise NotImplementedError
