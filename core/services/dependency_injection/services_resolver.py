from core.services.dependency_injection.services_injector import ServicesInjector
from core.services.base.open_ai_service_base import OpenAiServiceBase
from core.services.base.api_key_service_base import ApiKeyServiceBase


class ServicesResolver:

    __services_injector: ServicesInjector = ServicesInjector()

    @classmethod
    def get_open_ai_service(cls) -> OpenAiServiceBase:
        return cls.__services_injector.injector().get(OpenAiServiceBase)

    @classmethod
    def get_api_key_service(cls) -> ApiKeyServiceBase:
        return cls.__services_injector.injector().get(ApiKeyServiceBase)
