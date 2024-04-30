from src.model.password import Password


async def check_password(password: Password) -> bool:
    if password.length == 0:
        return False

    password_tuple: tuple = (
        password.numbers,
        password.low_case,
        password.up_case,
        password.special_char_1,
        password.special_char_2
    )

    return True in password_tuple
