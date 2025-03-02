from abc import ABC, abstractmethod

from core.data.models.keys.api_key_model import ApiKeyModel


class ApiKeyServiceBase(ABC):

    @abstractmethod
    async def get_api_key(self) -> ApiKeyModel:
        pass
