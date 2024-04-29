import pytest

from fastapi import HTTPException

from tests.mocks.passwords import (
    password_error_one,
    password_error_two,
    password_error_three,
    password_error_four,
)

from src.model.password import Password

from src.controller.controller_password import ControllerPassword


@pytest.mark.asyncio(scope="class")
class TestControllerErrorsLayer:
    controller_password: ControllerPassword = ControllerPassword()

    @pytest.mark.asyncio
    async def test_controller_password_error_one(self) -> None:
        pass_one: Password = Password.parse_obj(password_error_one)

        with pytest.raises(HTTPException):
            result = await self.controller_password.generate_password(pass_one)

            assert result.status_code == 400

    @pytest.mark.asyncio
    async def test_controller_password_error_two(self) -> None:
        pass_two: Password = Password.parse_obj(password_error_two)

        with pytest.raises(HTTPException):
            result = await self.controller_password.generate_password(pass_two)

            assert result.status_code == 400

    @pytest.mark.asyncio
    async def test_controller_password_error_three(self) -> None:
        pass_three: Password = Password.parse_obj(password_error_three)

        with pytest.raises(HTTPException):
            result = await self.controller_password.generate_password(pass_three)

            assert result.status_code == 400

    @pytest.mark.asyncio
    async def test_controller_password_error_four(self) -> None:
        pass_four: Password = Password.parse_obj(password_error_four)

        with pytest.raises(HTTPException):
            result = await self.controller_password.generate_password(pass_four)

            assert result.status_code == 400
