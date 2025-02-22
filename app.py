import uvicorn

from fastapi import FastAPI
from utils.helpers.enums import ServiceType

from api.api_server import ApiServer
from core.services.locator.services_injector import ServicesInjector


def main():
    # use ServiceType.MOCK to run with mock dependencies and data
    # use ServiceType.PROD to run with production dependencies and data

    services_injector: ServicesInjector = ServicesInjector(
        service_type=ServiceType.PROD
    )

    # initializing services
    services_injector.init()

    api_server: ApiServer = ApiServer(
        services_injector=services_injector,
        fast_api=FastAPI(
            docs_url="/api",
            title="OpenAI.API",
        ),
    )

    # running uvicorn server programatically
    uvicorn.run(api_server.app, host="localhost", port=8040)


if __name__ == "__main__":
    main()
