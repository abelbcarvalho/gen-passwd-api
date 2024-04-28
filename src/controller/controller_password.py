from src.model.password import Password
from src.service.service_password import ServicePassword


class ControllerPassword:
    _service: ServicePassword

    def __init__(self):
        self._service = ServicePassword()

    async def generate_password(self, password: Password) -> str | None:
        return await self._service.generate_password(password=password)
