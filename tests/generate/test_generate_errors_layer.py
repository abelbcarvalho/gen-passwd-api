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
        pass

    @pytest.mark.asyncio
    async def test_generate_password_error_two(self) -> None:
        pass

    @pytest.mark.asyncio
    async def test_generate_password_error_three(self) -> None:
        pass

    @pytest.mark.asyncio
    async def test_generate_password_error_four(self) -> None:
        pass
