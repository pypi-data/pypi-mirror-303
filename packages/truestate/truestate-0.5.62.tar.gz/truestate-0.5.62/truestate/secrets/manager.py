import typing
import uuid


from truestate.secrets.models import Secret


class SecretManager:
    def __init__(self, client):
        self.client = client

    def create_secret(self, secret) -> Secret:
        status_code, response = self.client.post(
            "/secrets/",
            data=secret,
        )
        return response.json()

    def get_secret(self, secret_id: uuid.UUID) -> Secret:
        status_code, response = self.client.get(f"/secrets/{secret_id}/")
        return response.json()

    def get_secrets(self) -> typing.List[Secret]:
        status_code, response = self.client.get("/secrets/")
        secrets = response.json()
        return [Secret(**secret) for secret in secrets]

    def delete_secret(self, secret_id: uuid.UUID) -> None:
        status_code, response = self.client.delete(f"/secrets/{secret_id}/")
        return response.json()

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        return self.get_secrets()
