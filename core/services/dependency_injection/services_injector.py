from injector import Injector
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

    @property
    def injector_prod(self) -> Injector:
        return self.__injector

    @property
    def injector_mock(self) -> Injector:
        return self.__injector_mock

    # Used prod and mock injectors to make it easier to debug/test and to be more maintainable.
    # By default is_production is set to true, since there's no need to initialize mock services on production.
    # To use mock services as well, pass is_production=False when calling the method. Then both mock and prod services will be initialized.

    def init(self, is_production: bool = True):

        # PROD INJECTIONS
        if self.__injector is None:
            self.__injector = Injector(
                [ServiceModule()],
                auto_bind=False,
            )

        if not is_production:
            print("Debug mode enabled")

            # MOCK INJECTIONS
            if self.__injector_mock is None:
                self.__injector_mock = Injector(
                    [ServiceMockModule()],
                    auto_bind=False,
                )
        else:
            print("Production mode enabled")
