from fastapi import APIRouter, HTTPException

from core.services.base.api_key_service_base import ApiKeyServiceBase
from utils.models.keys.api_key_model import ApiKeyModel


class ApiKeyApi:
    def __init__(self, router: APIRouter, api_key_service: ApiKeyServiceBase):
        self.router = router
        self.routes_setup()
        self.api_key_service = api_key_service

    def routes_setup(self):
        @self.router.get("/", tags=["API keys"])
        async def get_api_key() -> ApiKeyModel:
            try:
                return await self.api_key_service.get_api_key()
            except Exception as e:
                raise HTTPException(status_code=400, detail=str(e)) from e
