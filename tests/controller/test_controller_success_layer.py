import pytest

from tests.mocks.passwords import (
    password_one,
    password_two,
    password_three,
    password_four,
)

from src.model.password import Password


@pytest.mark.asyncio(scope="class")
class TestControllerSuccessLayer:
    _pass_one: Password = Password.parse_obj(password_one)
    _pass_two: Password = Password.parse_obj(password_two)
    _pass_three: Password = Password.parse_obj(password_three)
    _pass_four: Password = Password.parse_obj(password_four)

    @pytest.mark.asyncio
    async def test_controller_password_success_one(self) -> None:
        pass

    @pytest.mark.asyncio
    async def test_controller_password_success_two(self) -> None:
        pass

    @pytest.mark.asyncio
    async def test_controller_password_success_three(self) -> None:
        pass

    @pytest.mark.asyncio
    async def test_controller_password_success_four(self) -> None:
        pass
