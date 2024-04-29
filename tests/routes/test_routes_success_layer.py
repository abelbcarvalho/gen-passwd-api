from fastapi.testclient import TestClient

from tests.conftest import client

from tests.mocks.passwords import (
    password_one,
    password_two,
    password_three,
    password_four,
)


URL = "/api/generate/password"


async def test_generate_password_success_one(client: TestClient) -> None:
    response = client.post(URL, data=password_one)

    assert response.status_code == 201
