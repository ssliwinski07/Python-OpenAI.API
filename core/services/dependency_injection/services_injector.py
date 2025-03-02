from injector import Injector

from utils.helpers.enums import ServiceType
from core.services.dependency_injection.service_modules import (
    ServiceModule,
    ServiceMockModule,
)


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class ServicesInjector:

    def __init__(self):
        self.__injector: Injector = None
        self.__injector_mock: Injector = None
        self.service_type: ServiceType = None

    # Added one general injector that returns the correct one based on the service_type
    # so the whole app could use prod services/mock services.
    # Added separate mock injector and prod injector in case when we need to test only one
    # service with mock data and the rest should remain production.
    # To set only one serivce as a mock/prod, change the injector in ServicesResolver class
    # Thanks to that, dependency injection is more elastic and maintainable.

    def injector(self) -> Injector:

        match self.service_type:
            case ServiceType.PROD:
                return self.__injector
            case ServiceType.MOCK:
                return self.__injector_mock

    @property
    def injector_prod(self) -> Injector:
        return self.__injector

    @property
    def injector_mock(self) -> Injector:
        return self.__injector_mock

    def init(self, service_type: ServiceType = ServiceType.PROD):

        self.service_type = service_type

        # PROD INJECTIONS
        if self.__injector is None:
            self.__injector = Injector(
                [ServiceModule()],
                auto_bind=False,
            )

        # MOCK INJECTIONS
        if self.__injector_mock is None:
            self.__injector_mock = Injector(
                [ServiceMockModule()],
                auto_bind=False,
            )
