import pytest

from src.exceptions.exceptions import PasswordCheckerException

from src.model.password import Password

from tests.mocks.passwords import (
    password_one,
    password_two,
    password_three,
    password_four
)

from tests.service.generate_password_service import generate_password


@pytest.mark.asyncio(scope="class")
class TestServiceSuccessLayer:
    pass
