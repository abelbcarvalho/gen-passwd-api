from pydantic import BaseModel
from typing import Optional


class Password(BaseModel):
    numbers: Optional[bool] = None
    low_case: Optional[bool] = None
    up_case: Optional[bool] = None
    special_char_1: Optional[bool] = None
    special_char_2: Optional[bool] = None
    length: int = 0
