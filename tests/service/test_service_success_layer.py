import pytest

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
        new_password = await generate_password(password_one)

        assert new_password is not None
        assert type(new_password) is str
        assert len(new_password) == password_one["length"]

    @pytest.mark.asyncio
    async def test_password_service_success_two(self) -> None:
        new_password = await generate_password(password_two)

        assert new_password is not None
        assert type(new_password) is str
        assert len(new_password) == password_two["length"]

    @pytest.mark.asyncio
    async def test_password_service_success_three(self) -> None:
        new_password = await generate_password(password_three)

        assert new_password is not None
        assert type(new_password) is str
        assert len(new_password) == password_three["length"]

    @pytest.mark.asyncio
    async def test_password_service_success_four(self) -> None:
        new_password = await generate_password(password_four)

        assert new_password is not None
        assert type(new_password) is str
        assert len(new_password) == password_four["length"]
