from abc import ABC, abstractmethod


class ApiKeyServiceBase(ABC):
    @abstractmethod
    def get_api_key(self):
        pass
