import pytest

from os import environ

from httpx import AsyncClient

from tests.mocks.passwords import (
    password_one,
    password_error_one,
    password_error_two,
    password_error_three,
    password_error_four
)

from src.app.app import app


URL = "/api/generate/password"
API_URL_BASE = environ["API_URL_BASE_TEST"]


@pytest.mark.asyncio(scope="class")
class TestRoutesErrorsLayer:
    @pytest.mark.asyncio
    async def test_routes_errors_layer_one(self) -> None:
        async with AsyncClient(app=app, base_url=API_URL_BASE) as client:
            response = await client.post(
                url=URL,
                json=password_error_one
            )

            assert response.status_code == 400

    @pytest.mark.asyncio
    async def test_routes_errors_layer_two(self) -> None:
        async with AsyncClient(app=app, base_url=API_URL_BASE) as client:
            response = await client.post(
                url=URL,
                json=password_error_two
            )

            assert response.status_code == 400

    @pytest.mark.asyncio
    async def test_routes_errors_layer_three(self) -> None:
        async with AsyncClient(app=app, base_url=API_URL_BASE) as client:
            response = await client.post(
                url=URL,
                json=password_error_three
            )

            assert response.status_code == 400

    @pytest.mark.asyncio
    async def test_routes_errors_layer_four(self) -> None:
        password_error = password_one

        password_error["length"] = 0

        async with AsyncClient(app=app, base_url=API_URL_BASE) as client:
            response = await client.post(
                url=URL,
                json=password_error
            )

            assert response.status_code == 400

    @pytest.mark.asyncio
    async def test_routes_errors_layer_five(self) -> None:
        async with AsyncClient(app=app, base_url=API_URL_BASE) as client:
            response = await client.post(
                url=URL,
                json=password_error_four
            )

            assert response.status_code == 400
