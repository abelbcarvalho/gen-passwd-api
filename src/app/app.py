import uvicorn

from fastapi import FastAPI

from src.routes.routes import passwd_generator_api


# definition
app = FastAPI()
app.include_router(passwd_generator_api)


# run api
async def handle_api() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8000)
