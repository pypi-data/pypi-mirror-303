import typing
import uuid

from truestate.artifacts.classification import ClassHierarchy, Category

SUPPORTED_ARTIFACT_TYPES = [ClassHierarchy]


def to_server_syntax(artifact: ClassHierarchy) -> dict:
    return artifact.dict()


def to_client_syntax(data: dict) -> ClassHierarchy:
    return ClassHierarchy(
        id=data.get("id"),
        name=data["name"],
        choices=[
            server_to_client_syntax(choice)
            for choice in data["classification_classes"]["subcategories"]
        ],
    )


def server_to_client_syntax(data: dict) -> Category:
    return Category(
        label=data["label"],
        criteria=data["criteria"],
        subcategories=[
            server_to_client_syntax(subcategory)
            for subcategory in data["subcategories"]
        ],
    )


class ArtifactsManager:
    
    def __init__(self, client):
        self.client = client

    def sync(self, artifact):
        
        if isinstance(artifact, ClassHierarchy):
            return self._create_classification_class(artifact)
        else:
            raise ValueError(
                f"Unexpected artifact type `{type(artifact)}` expected on of {SUPPORTED_ARTIFACT_TYPES}"
            )

    def _create_classification_class(self, artifact):

        status_code, result = self.client.post(
            "/classification-classes/",
            data=to_server_syntax(artifact),
        )

        if status_code == 409:
            return self._update_classification_class(new_artifact=artifact)

        elif status_code == 422:
            raise ValueError(result)

        data = to_client_syntax(result)

        return data

    def _update_classification_class(self, new_artifact: ClassHierarchy):
        # get the artifact first...
        current_artifact = self.get(name=new_artifact.name)

        if current_artifact.name == new_artifact.name and self._compare_ignoring_uuids(
            current_artifact, new_artifact
        ):
            # there is no change so don't update the artifact
            data = current_artifact.dict()

            return to_client_syntax(data)

        else:
            # update
            body = {"id": current_artifact.id, **to_server_syntax(new_artifact)}
            status_code, result = self.client.patch(
                f"/classification-classes/{current_artifact.id}/",
                data=body,
            )

            print(result)

            return to_client_syntax(result)

    def _compare_ignoring_uuids(
        self,
        hierarchy_1: ClassHierarchy,
        hierarchy_2: ClassHierarchy,
    ):
        def _recurisive_id_removal(hierarchy: dict):
            hierarchy.pop("id")

            if len(hierarchy["subcategories"]) == 0:
                return hierarchy
            else:
                hierarchy["subcategories"] = [
                    _recurisive_id_removal(subcategory)
                    for subcategory in hierarchy["subcategories"]
                ]
                return hierarchy

        dict_1 = _recurisive_id_removal(hierarchy_1.dict()["classification_classes"])
        dict_2 = _recurisive_id_removal(hierarchy_2.dict()["classification_classes"])

        same_names = hierarchy_1.name == hierarchy_2.name
        same_content = dict_1 == dict_2

        if same_names & same_content:
            return True
        else:
            return False

    def get(self, id: uuid.UUID = None, name: str = None):
        return self._get_classification_class(id=id, name=name)

    def _get_classification_class(self, id: uuid.UUID = None, name: str = None):
        if not id and not name:
            status_code, result = self.client.get(
                "/classification-classes/",
            )

            if status_code == 404:
                return None

            return [to_client_syntax(record) for record in result]

        elif id:
            status_code, result = self.client.get(
                "/classification-classes/{id}",
            )

            if status_code == 404:
                return None

            return to_client_syntax(result)

        elif name:
            status_code, result = self.client.get(
                f"/classification-classes/?name={name}",
            )

            if status_code == 404:
                return None

            if len(result) == 0:
                return None

            elif len(result) > 1:
                raise Exception(
                    f"Multiple classification classes found with name `{name}`"
                )

            else:
                return to_client_syntax(result[0])

        else:
            raise Exception("How did we get here...")

    def delete(self, id: uuid.UUID = None, name: str = None):
        return self._delete_classification_class(id=id, name=name)

    def _delete_classification_class(self, id: uuid.UUID, name: str = None):
        if id:
            status_code, result = self.client.delete(
                "/classification-classes/{id}",
            )

            if status_code == 404:
                return None

            return ClassHierarchy(**result)

        elif name:
            # look up by name
            status_code, result = self.client.get(
                f"/classification-classes/?name={name}",
            )

            if status_code == 404:
                return None

            if len(result) == 0:
                return None

            # elif len(result) > 1:
            #     raise Exception(
            #         f"Multiple classification classes found with name `{name}`"
            #     )

            else:
                for record in result:
                    status_code, result = self.client.delete(
                        f"/classification-classes/{record['id']}",
                    )

        else:
            raise ValueError(
                "Either `id` or `name` must be provided to delete a CategoryHierarchy"
            )

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        return self.get(*args, **kwargs)
