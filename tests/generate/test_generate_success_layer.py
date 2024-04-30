import pytest

from src.model.password import Password

from src.generate.generate import Generate

from tests.mocks.passwords import (
    password_one,
    password_two,
    password_three,
    password_four
)


@pytest.mark.asyncio(scope="class")
class TestGenerateSuccessful:
    generate: Generate = Generate()

    @pytest.mark.asyncio
    async def test_password_generate_success_one(self) -> None:
        pass_one = Password.parse_obj(password_one)

        new_password = await self.generate.generate_password(pass_one)

        assert new_password is not None
        assert isinstance(new_password, str)
        assert len(new_password) == pass_one.length

    @pytest.mark.asyncio
    async def test_password_generate_success_two(self) -> None:
        pass_two = Password.parse_obj(password_two)

        new_password = await self.generate.generate_password(pass_two)

        assert new_password is not None
        assert isinstance(new_password, str)
        assert len(new_password) == pass_two.length

    @pytest.mark.asyncio
    async def test_password_generate_success_three(self) -> None:
        pass_three = Password.parse_obj(password_three)

        new_password = await self.generate.generate_password(pass_three)

        assert new_password is not None
        assert isinstance(new_password, str)
        assert len(new_password) == pass_three.length

    @pytest.mark.asyncio
    async def test_password_generate_success_four(self) -> None:
        pass_four = Password.parse_obj(password_four)

        new_password = await self.generate.generate_password(pass_four)

        assert new_password is not None
        assert isinstance(new_password, str)
        assert len(new_password) == pass_four.length
