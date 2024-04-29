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
        pass

    @pytest.mark.asyncio
    async def test_password_generate_success_two(self) -> None:
        pass

    @pytest.mark.asyncio
    async def test_password_generate_success_three(self) -> None:
        pass

    @pytest.mark.asyncio
    async def test_password_generate_success_four(self) -> None:
        pass
