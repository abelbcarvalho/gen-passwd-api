import pytest

from src.model.password import Password

from src.generate.generate import Generate

from tests.mocks.passwords import (
    password_error_one,
    password_error_two,
    password_error_three,
    password_error_four
)


@pytest.mark.asyncio(scope="class")
class TestGenerateErrorsLayer:
    generate: Generate = Generate()

    @pytest.mark.asyncio
    async def test_generate_password_error_one(self) -> None:
        pass_error_one = Password.parse_obj(password_error_one)

        new_password = await self.generate.generate_password(pass_error_one)

        assert len(new_password) == 0

    @pytest.mark.asyncio
    async def test_generate_password_error_two(self) -> None:
        pass_error_two = Password.parse_obj(password_error_two)

        new_password = await self.generate.generate_password(pass_error_two)

        assert len(new_password) == 0

    @pytest.mark.asyncio
    async def test_generate_password_error_three(self) -> None:
        pass_error_three = Password.parse_obj(password_error_three)

        new_password = await self.generate.generate_password(pass_error_three)

        assert len(new_password) == 0

    @pytest.mark.asyncio
    async def test_generate_password_error_four(self) -> None:
        pass_error_four = Password.parse_obj(password_error_four)

        new_password = await self.generate.generate_password(pass_error_four)

        assert len(new_password) == 0
