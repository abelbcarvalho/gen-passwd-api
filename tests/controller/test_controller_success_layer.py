import pytest

from tests.mocks.passwords import (
    password_one,
    password_two,
    password_three,
    password_four,
)

from src.model.password import Password

from src.controller.controller_password import ControllerPassword


@pytest.mark.asyncio(scope="class")
class TestControllerSuccessLayer:
    controller_password: ControllerPassword = ControllerPassword()

    @pytest.mark.asyncio
    async def test_controller_password_success_one(self) -> None:
        pass_one: Password = Password.parse_obj(password_one)

        result = await self.controller_password.generate_password(pass_one)

    @pytest.mark.asyncio
    async def test_controller_password_success_two(self) -> None:
        pass_two: Password = Password.parse_obj(password_two)

        result = await self.controller_password.generate_password(pass_two)

    @pytest.mark.asyncio
    async def test_controller_password_success_three(self) -> None:
        pass_three: Password = Password.parse_obj(password_three)

        result = await self.controller_password.generate_password(pass_three)

    @pytest.mark.asyncio
    async def test_controller_password_success_four(self) -> None:
        pass_four: Password = Password.parse_obj(password_four)

        result = await self.controller_password.generate_password(pass_four)
