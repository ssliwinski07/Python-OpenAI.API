from fastapi import APIRouter, HTTPException, Depends

from core.services.base.api_key_service_base import ApiKeyServiceBase
from core.data.models.keys.api_key_model import ApiKeyModel
from core.services.dependency_injection.services_resolver import ServicesResolver
from utils.helpers.enums import ServiceType


class ApiKeyApi:
    def __init__(
        self,
        router: APIRouter,
    ):
        self.router = router
        self.routes_setup()

    # By default service_type in get_api_key_service method is set to PROD, so PROD service
    # is being fetched. However, if you want to use mock service, just change service_type parameter
    # ServicesResolver methods are managing which service should be fetched based on service_type parameter
    def get_api_key_service(self) -> ApiKeyServiceBase:
        return ServicesResolver.get_api_key_service()

    def routes_setup(self):
        @self.router.get("/", tags=["API keys"])

        # used dependency injection concept from FastAPI
        async def get_api_key(
            api_key_service: ApiKeyServiceBase = Depends(self.get_api_key_service),
        ) -> ApiKeyModel:
            try:
                return await api_key_service.get_api_key()
            except Exception as e:
                raise HTTPException(status_code=400, detail=str(e)) from e
