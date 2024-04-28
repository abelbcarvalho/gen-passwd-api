from pydantic import BaseModel


class Password(BaseModel):
    numbers: bool = None
    low_case: bool = None
    up_case: bool = None
    special_char_1: bool = None
    special_char_2: bool = None
    length: int = 0
