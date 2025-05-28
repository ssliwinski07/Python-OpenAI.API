from core.services.dependency_injection.services_injector import ServicesInjector
from core.services.base.open_ai_service_base import OpenAiServiceBase
from core.services.base.api_key_service_base import ApiKeyServiceBase
from utils.helpers.enums import ServiceType


class ServicesResolver:

    __services_injector: ServicesInjector = ServicesInjector()

    # In the following methods service_type paramater is used to choose which service to return - prod or mock.
    # By default it should be set to ServiceType.PROD. If you want to use mock service, set it to ServiceType.MOCK when calling the method.
    # It was desgined that way for debbuging/testing purposes - in case if only one service should be mocked and the rest should remain prod.

    @classmethod
    def get_open_ai_service(
        cls, service_type: ServiceType = ServiceType.PROD
    ) -> OpenAiServiceBase:
        match service_type:
            case ServiceType.PROD:
                return cls.__services_injector.injector_prod.get(OpenAiServiceBase)
            case ServiceType.MOCK:
                return cls.__services_injector.injector_mock.get(OpenAiServiceBase)

    @classmethod
    def get_api_key_service(
        cls, service_type: ServiceType = ServiceType.PROD
    ) -> ApiKeyServiceBase:
        match service_type:
            case ServiceType.PROD:
                return cls.__services_injector.injector_prod.get(ApiKeyServiceBase)
            case ServiceType.MOCK:
                return cls.__services_injector.injector_mock.get(ApiKeyServiceBase)
