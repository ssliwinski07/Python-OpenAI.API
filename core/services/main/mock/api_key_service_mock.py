from injector import singleton

from core.services.base.api_key_service_base import ApiKeyServiceBase
from utils.models.keys.api_key_model import ApiKeyModel


@singleton
class ApiKeyServiceMock(ApiKeyServiceBase):

    def get_api_key(self) -> ApiKeyModel:
        return ApiKeyModel(api_key="uk-124234xxvfqszcfteest")
