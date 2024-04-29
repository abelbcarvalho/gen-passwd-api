from src.utility.password_checker import PasswordChecker

from src.model.password import Password

from src.generate.generate import Generate

from src.exceptions.exceptions import PasswordCheckerException


async def generate_password(password: dict) -> str:
    payload = Password.parse_obj(password)

    generate: Generate = Generate()

    if not await PasswordChecker.check_password(password=payload):
        raise PasswordCheckerException("generate length or generate params whole false")

    new_password = await generate.generate_password(password=payload)

    return new_password
