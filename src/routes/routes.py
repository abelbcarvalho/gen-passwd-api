from fastapi import APIRouter, Response

from src.model.password import Password
from src.controller.controller_password import ControllerPassword


# definition
passwd_generator_api = APIRouter()
controller = ControllerPassword()


@passwd_generator_api.post("/api/generate/password")
async def generate_password(password: Password) -> Response:
    return await controller.generate_password(password=password)
