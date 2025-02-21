import uvicorn
from fastapi import FastAPI

from api.api_server import ApiServer
from core.services.locator.service_locator import ServicesInjector


def main():
    # services initialization
    ServicesInjector.init()

    api_server = ApiServer(
        fast_api=FastAPI(
            docs_url="/api",
            title="OpenAI.API",
        )
    )
    # running uvicorn server programatically
    uvicorn.run(api_server.app, host="localhost", port=8040)


if __name__ == "__main__":
    main()
