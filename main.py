import asyncio

from src.app.app import handle_api


if __name__ == '__main__':
    asyncio.run(handle_api())
