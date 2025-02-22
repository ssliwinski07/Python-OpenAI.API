from core.services.base.api_key_service_base import ApiKeyServiceBase
from core.services.locator.services_injector import ServicesInjector
from api.keys.api_key_api import ApiKeyApi
from api.users.users_api import UsersAPI
from utils.models.routes.routes_container_model import RoutesContainerModel


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
            ApiKeyApi(
                router=self.routers.public.api_key,
                api_key_service=self.services_injector.injector().get(
                    ApiKeyServiceBase
                ),
            )
            self.__is_initialized = True
