import pytest

from os import environ

from httpx import AsyncClient

from tests.mocks.passwords import (
    password_one,
    password_two,
    password_three,
    password_four,
)

from src.app.app import app


URL = "/api/generate/password"
API_URL_BASE = environ["API_URL_BASE_TEST"]


@pytest.mark.asyncio(scope="class")
class TestRoutesSuccessLayer:
    @pytest.mark.asyncio
    async def test_routes_generate_password_success_one(self) -> None:
        password_one["length"] = 32

        async with AsyncClient(app=app, base_url=API_URL_BASE) as client:
            response = await client.post(
                url=URL,
                json=password_one
            )

            assert response.status_code == 201

    @pytest.mark.asyncio
    async def test_routes_generate_password_success_two(self) -> None:
        async with AsyncClient(app=app, base_url=API_URL_BASE) as client:
            response = await client.post(
                url=URL,
                json=password_two
            )

            assert response.status_code == 201

    @pytest.mark.asyncio
    async def test_routes_generate_password_success_three(self) -> None:
        async with AsyncClient(app=app, base_url=API_URL_BASE) as client:
            response = await client.post(
                url=URL,
                json=password_three
            )

            assert response.status_code == 201

    @pytest.mark.asyncio
    async def test_routes_generate_password_success_four(self) -> None:
        async with AsyncClient(app=app, base_url=API_URL_BASE) as client:
            response = await client.post(
                url=URL,
                json=password_four
            )

            assert response.status_code == 201
