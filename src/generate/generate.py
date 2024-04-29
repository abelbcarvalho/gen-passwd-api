from random import choice

from src.model.password import Password
from src.utility.password_utility import get_not_none_keys


class Generate:
    _numbers: tuple[str, ...]
    _low_case: tuple[str, ...]
    _up_case: tuple[str, ...]
    _special_char_1: tuple[str, ...]
    _special_char_2: tuple[str, ...]

    def __init__(self):
        self._numbers = tuple(str(v) for v in range(10))
        self._low_case = tuple(chr(v) for v in range(97, 123))
        self._up_case = tuple(chr(v) for v in range(65, 91))
        self._special_char_1 = tuple(v for v in "!#$%&()*+,-./:;=?@[]{|}")
        self._special_char_2 = tuple(v for v in "<>^~¢£§¬")

    async def generate_password(self, password: Password) -> str | None:
        not_none_keys = await get_not_none_keys(password=password)

        valid_keys: tuple = tuple(v for v in not_none_keys)

        new_password: str = len(valid_keys) > 0 and await self._join_str_password(
            length=password.length,
            valid_keys=valid_keys,
        ) or ""

        return new_password

    async def _join_str_password(self, length: int, valid_keys: tuple[str]) -> str:
        data_to_select: dict = {
            "numbers": self._numbers,
            "low_case": self._low_case,
            "up_case": self._up_case,
            "special_char_1": self._special_char_1,
            "special_char_2": self._special_char_2,
        }

        passwd = ""

        for _ in range(length):
            chosen_key: str = choice(valid_keys)

            chosen_value: str = choice(data_to_select.get(chosen_key))

            passwd += chosen_value

        return passwd
