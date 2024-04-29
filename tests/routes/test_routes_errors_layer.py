import pytest

from os import environ

from httpx import AsyncClient

from tests.mocks.passwords import (
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
        pass

    @pytest.mark.asyncio
    async def test_routes_errors_layer_two(self) -> None:
        pass

    @pytest.mark.asyncio
    async def test_routes_errors_layer_three(self) -> None:
        pass

    @pytest.mark.asyncio
    async def test_routes_errors_layer_four(self) -> None:
        pass
