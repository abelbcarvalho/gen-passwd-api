from fastapi import Response

from src.model.password import Password
from src.generate.generate import Generate
from src.exceptions.exceptions import PasswordCheckerException
from src.utility.password_checker import check_password
from src.utility.response import (
    error_response,
    success_response,
)


class ServicePassword:
    _generate: Generate

    def __init__(self):
        self._generate = Generate()

    async def generate_password(self, password: Password) -> Response | None:
        try:
            if not await check_password(password=password):
                raise PasswordCheckerException("generate length or generate params whole false")
        except PasswordCheckerException as pce:
            await error_response(key="error", value=pce.args[0], status_code=400)

        new_password = await self._generate.generate_password(password=password)

        return await success_response(key="password", value=new_password, status_code=201)
