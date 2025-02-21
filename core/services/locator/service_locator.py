from injector import Injector, Module, singleton, provider

from core.services.base.api_key_service_base import ApiKeyServiceBase
from core.services.main.production.api_key_service import ApiKeyService
from core.services.main.mock.api_key_service_mock import ApiKeyServiceMock
from utils.helpers.enums import ServiceType


class ServiceLocatorModule(Module):

    def configure(self, binder):
        binder.bind(ApiKeyServiceBase, to=ApiKeyService, scope=singleton)

    @provider
    @singleton
    def provide_api_key_service(self) -> ApiKeyServiceBase:
        return ApiKeyService()


class ServiceLocatorMockModule(Module):

    def configure(self, binder):
        binder.bind(ApiKeyServiceBase, to=ApiKeyServiceMock, scope=singleton)

    @provider
    @singleton
    def provide_api_key_service(self) -> ApiKeyServiceBase:
        return ApiKeyServiceMock()


class ServicesInjector:

    __injector: Injector = None
    __injector_mock: Injector = None

    @classmethod
    def injector(cls, service_type: ServiceType) -> Injector:

        match service_type:
            case ServiceType.PROD:
                return cls.__injector
            case ServiceType.MOCK:
                return cls.__injector_mock

    @classmethod
    def init(cls):

        # PROD INJECTIONS
        if cls.__injector is None:
            cls.__injector = Injector(
                [ServiceLocatorModule()],
                auto_bind=False,
            )

        # MOCK INJECTIONS
        if cls.__injector_mock is None:
            cls.__injector_mock = Injector(
                [ServiceLocatorMockModule()],
                auto_bind=False,
            )
