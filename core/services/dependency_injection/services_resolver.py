from core.services.dependency_injection.services_injector import ServicesInjector
from core.services.base.open_ai_service_base import OpenAiServiceBase
from core.services.base.api_key_service_base import ApiKeyServiceBase
from utils.helpers.enums import ServiceType


class ServicesResolver:

    __services_injector: ServicesInjector = ServicesInjector()

    @classmethod
    def get_open_ai_service(
        cls, service_type: ServiceType = ServiceType.PROD
    ) -> OpenAiServiceBase:
        match service_type:
            case ServiceType.PROD:
                return cls.__services_injector.injector().get(OpenAiServiceBase)
            case ServiceType.MOCK:
                return cls.__services_injector.injector_mock.get(OpenAiServiceBase)

    @classmethod
    def get_api_key_service(
        cls, service_type: ServiceType = ServiceType.PROD
    ) -> ApiKeyServiceBase:
        match service_type:
            case ServiceType.PROD:
                return cls.__services_injector.injector().get(ApiKeyServiceBase)
            case ServiceType.MOCK:
                return cls.__services_injector.injector_mock.get(ApiKeyServiceBase)
