import pytest

from src.exceptions.exceptions import PasswordCheckerException

from src.model.password import Password

from tests.mocks.passwords import (
    password_error_one,
    password_error_two,
    password_error_three,
    password_error_four
)

from tests.service.generate_password_service import generate_password


@pytest.mark.asyncio(scope="class")
class TestServiceErrorsLayer:
    pass
