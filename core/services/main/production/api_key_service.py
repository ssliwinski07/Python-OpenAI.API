import os
from injector import singleton

from core.services.base.api_key_service_base import ApiKeyServiceBase
from core.localization.localizations import Localizations
from core.data.models.keys.api_key_model import ApiKeyModel
from utils.messages import messages
from utils.helpers.consts import API_KEY


@singleton
class ApiKeyService(ApiKeyServiceBase):

    async def get_api_key(self) -> ApiKeyModel:
        try:
            api_key = os.getenv(API_KEY)
            if not api_key:
                raise ValueError(
                    Localizations.translate(msg=messages.API_KEY_NOT_FOUND)
                )
            return ApiKeyModel(api_key=api_key)
        except Exception as e:
            raise ValueError(
                f"{Localizations.translate(msg=messages.GETTING_API_KEY_ERROR)} - {e}"
            ) from e
