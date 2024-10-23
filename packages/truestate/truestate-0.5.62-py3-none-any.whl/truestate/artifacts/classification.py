import uuid

import pydantic


class Category(pydantic.BaseModel):
    """
    A recursive model for representing a category tree. Each category represents a class for classification.
    If a category has subcategories, the subcategories are also represented as
    Category objects, forming a recursive tree structure.
    """

    id: str = pydantic.Field(
        title="ID",
        description="The unique identifier for the category.",
        default_factory=lambda: str(uuid.uuid4()),
    )
    label: str = pydantic.Field(
        ..., title="Label", description="The label for the category."
    )
    criteria: str = pydantic.Field(
        ..., title="Criteria", description="The criteria for the category."
    )
    subcategories: list["Category"] = pydantic.Field(
        default=[], title="Subcategories", description="A list of subcategories."
    )

    def dict(self):
        data = {
            "id": self.id,
            "label": self.label,
            "criteria": self.criteria,
            "subcategories": [sub.dict() for sub in self.subcategories],
        }

        return data


class ServerCategoryHierarchyModel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid", arbitrary_types_allowed=True)

    name: str
    classification_classes: Category


class ClassHierarchy:
    def __init__(
        self,
        name: str,
        choices: list[Category],
        id: str | None = None,
    ):
        self.name = name
        self.choices = choices
        self.id = id

    def dict(self):
        data = {
            "name": self.name,
            "classification_classes": {
                "id": "root",
                "label": "root",
                "criteria": "root",
                "subcategories": [choice.model_dump() for choice in self.choices],
            },
        }

        ServerCategoryHierarchyModel.model_validate(data)

        return data
