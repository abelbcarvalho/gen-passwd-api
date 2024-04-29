import pytest

from fastapi.testclient import TestClient

from src.app.app import app


@pytest.fixture(scope="function")
async def client() -> TestClient:
    with TestClient(app) as test:
        yield test
