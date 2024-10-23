class Dataset:
    def __init__(
        self,
        name: str = None,
        description: str = None,
    ) -> None:
        if name is None:
            raise ValueError("Please define a name for your dataset")
        else:
            self.name = name

        if description is None:
            description = ""

        self.description = description

    def dict(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
        }
