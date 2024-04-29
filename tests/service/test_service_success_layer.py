import pytest

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
    @pytest.mark.asyncio
    async def test_password_service_success_one(self) -> None:
        pass_one = Password.parse_obj(password_one)

    @pytest.mark.asyncio
    async def test_password_service_success_two(self) -> None:
        pass_two = Password.parse_obj(password_two)

    @pytest.mark.asyncio
    async def test_password_service_success_three(self) -> None:
        pass_three = Password.parse_obj(password_three)

    @pytest.mark.asyncio
    async def test_password_service_success_four(self) -> None:
        pass_four = Password.parse_obj(password_four)
