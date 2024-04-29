import pytest

from typing import Generator

from fastapi.testclient import TestClient

from src.app.app import app


@pytest.fixture(scope="function")
async def client() -> Generator:
    with TestClient(app) as test:
        yield test
