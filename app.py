import locale
import uvicorn
from fastapi import FastAPI

from utils.helpers.enums import ServiceType
from api.core.api_server import ApiServer
from core.services.dependency_injection.services_injector import ServicesInjector
from core.localization.localizations import Localizations


def main():

    # uncomment to get language code from system
    # lang = locale.getlocale()[0][:2]

    # localization initialization
    Localizations.lang_initialization(lang_code="en")

    services_injector: ServicesInjector = ServicesInjector()
    # initializing services
    # by default it will use production dependencies and data
    # if you want to use mock dependencies and data, set service_type parameter to ServiceType.MOCK
    services_injector.init()

    api_server: ApiServer = ApiServer(
        services_injector=services_injector,
        fast_api=FastAPI(docs_url="/docs", title="OpenAI.API", root_path="/api"),
    )

    # running uvicorn server programatically
    uvicorn.run(api_server.app, host="localhost", port=8040)


if __name__ == "__main__":
    main()
