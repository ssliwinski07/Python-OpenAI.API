from core.services.dependency_injection.services_injector import ServicesInjector
from core.data.models.routes.routes_container_model import RoutesContainerModel
from api.endpoints.keys.api_key_api import ApiKeyApi
from api.endpoints.users.users_api import UsersAPI
from api.endpoints.openAI.open_ai_api import OpenAIAPI


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class ApiInitializer:

    def __init__(
        self, routers: RoutesContainerModel, services_injector: ServicesInjector
    ) -> None:
        if not hasattr(self, "is_initialized"):
            self.routers = routers
            self.services_injector = services_injector
            self.__is_initialized = False

    def initialize(self) -> None:
        if not self.__is_initialized:
            UsersAPI(router=self.routers.private.users)
            OpenAIAPI(
                router=self.routers.private.open_ai,
            )
            ApiKeyApi(
                router=self.routers.public.api_key,
            )
            self.__is_initialized = True
