from typing import Any

from fastapi import Response


async def success_response(
        content: Any = None,
        key: str = "key",
        value: str = "value",
        status_code: int = 200
) -> Response:
    if content is None:
        content = {key: value}

    return Response(
        content=content,
        status_code=status_code
    )
