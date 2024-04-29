import pytest

from src.exceptions.exceptions import PasswordCheckerException

from tests.mocks.passwords import (
    password_error_one,
    password_error_two,
    password_error_three,
    password_error_four
)

from tests.service.generate_password_service import generate_password


@pytest.mark.asyncio(scope="class")
class TestServiceErrorsLayer:
    @pytest.mark.asyncio
    async def test_password_error_one(self) -> None:
        pass

    @pytest.mark.asyncio
    async def test_password_error_two(self) -> None:
        pass

    @pytest.mark.asyncio
    async def test_password_error_three(self) -> None:
        pass

    @pytest.mark.asyncio
    async def test_password_error_four(self) -> None:
        pass
