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
