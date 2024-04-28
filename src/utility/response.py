from typing import Any

from fastapi import Response, HTTPException


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


async def error_response(key: str, value: str, status_code: int) -> None:
    detail = {key: value}

    raise HTTPException(
        detail=detail,
        status_code=status_code,
    )
