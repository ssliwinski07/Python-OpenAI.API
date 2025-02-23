from abc import ABC, abstractmethod

from utils.models.keys.api_key_model import ApiKeyModel


class ApiKeyServiceBase(ABC):

    @abstractmethod
    def get_api_key(self) -> ApiKeyModel:
        pass
