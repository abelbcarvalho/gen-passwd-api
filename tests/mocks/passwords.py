password_one: dict = dict(
    numbers=True,
    low_case=True,
    up_case=True,
    special_char_1=True,
    special_char_2=True,
    length=32
)

password_two: dict = dict(
    numbers=True,
    low_case=True,
    up_case=True,
    length=32
)

password_three: dict = dict(
    numbers=True,
    low_case=True,
    special_char_1=True,
    length=32
)

password_four: dict = dict(
    numbers=True,
    low_case=True,
    special_char_2=True,
    length=32
)

password_error_one: dict = dict(length=32)

password_error_two: dict = dict(length=0)

password_error_three: dict = dict(
    numbers=True,
    length=0
)

password_error_four: dict = dict(
    numbers=True,
    up_case=True,
    low_case=True,
    special_char_1=True,
    special_char_2=True
)
