from injector import Module, singleton, provider

from core.services.main.production.api_key_service import ApiKeyService
from core.services.main.production.open_ai_service import OpenAiService
from core.services.base.api_key_service_base import ApiKeyServiceBase
from core.services.base.open_ai_service_base import OpenAiServiceBase
from core.services.main.mock.api_key_service_mock import ApiKeyServiceMock
from core.services.main.mock.open_ai_service_mock import OpenAiServiceMock


class ServiceLocatorModule(Module):

    def configure(self, binder):
        binder.bind(ApiKeyServiceBase, to=ApiKeyService, scope=singleton)
        binder.bind(OpenAiServiceBase, to=OpenAiService, scope=singleton)

    @provider
    @singleton
    def provide_api_key_service(self) -> ApiKeyServiceBase:
        return ApiKeyService()

    @provider
    @singleton
    def provide_open_ai_service(self) -> OpenAiServiceBase:
        return OpenAiService()


class ServiceLocatorMockModule(Module):

    def configure(self, binder):
        binder.bind(ApiKeyServiceBase, to=ApiKeyServiceMock, scope=singleton)
        binder.bind(OpenAiServiceBase, to=OpenAiServiceMock, scope=singleton)

    @provider
    @singleton
    def provide_api_key_service(self) -> ApiKeyServiceBase:
        return ApiKeyServiceMock()

    @provider
    @singleton
    def provide_open_ai_service(self) -> OpenAiServiceBase:
        return OpenAiServiceMock()
