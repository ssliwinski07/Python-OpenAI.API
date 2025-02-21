import os
from injector import singleton

from core.services.base.api_key_service_base import ApiKeyServiceBase
from utils.models.keys.api_key_model import ApiKeyModel


@singleton
class ApiKeyService(ApiKeyServiceBase):

    def get_api_key(self) -> ApiKeyModel:
        try:
            api_key = os.getenv("API_KEY")
            if not api_key:
                raise ValueError("API key not found")
            return ApiKeyModel(api_key=api_key)
        except Exception as e:
            raise ValueError(f"Error getting API key - {e}") from e
