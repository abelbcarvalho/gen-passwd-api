import uvicorn

from fastapi import FastAPI

from src.routes.routes import passwd_generator_api


# definition
app = FastAPI()
app.include_router(passwd_generator_api)


# run api
def handle_api() -> None:
    uvicorn.run("src.app.app:app", host="localhost", port=8000, reload=True)
