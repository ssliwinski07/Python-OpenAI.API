from injector import Injector

from utils.helpers.enums import ServiceType
from core.services.locator.service_locator import (
    ServiceLocatorModule,
    ServiceLocatorMockModule,
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

    def __init__(self, service_type: ServiceType):
        self.__injector: Injector = None
        self.__injector_mock: Injector = None
        self.service_type: ServiceType = service_type

    def injector(self) -> Injector:

        match self.service_type:
            case ServiceType.PROD:
                return self.__injector
            case ServiceType.MOCK:
                return self.__injector_mock

    def init(self):

        # PROD INJECTIONS
        if self.__injector is None:
            self.__injector = Injector(
                [ServiceLocatorModule()],
                auto_bind=False,
            )

        # MOCK INJECTIONS
        if self.__injector_mock is None:
            self.__injector_mock = Injector(
                [ServiceLocatorMockModule()],
                auto_bind=False,
            )
