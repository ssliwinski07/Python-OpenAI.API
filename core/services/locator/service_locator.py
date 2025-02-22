from injector import Module, singleton, provider

from core.services.base.api_key_service_base import ApiKeyServiceBase
from core.services.main.production.api_key_service import ApiKeyService
from core.services.main.mock.api_key_service_mock import ApiKeyServiceMock


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
