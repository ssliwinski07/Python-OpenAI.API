import os
from fastapi import FastAPI, APIRouter, HTTPException, Request, Depends, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import JSONResponse

from api.users.users_api import UsersAPI
from api.keys.api_key_api import ApiKeyApi
from utils.models.routers.root.root_router_model import RootRouterModel
from utils.models.errors.http_error_response_model import HttpErrorResponseModel
from utils.helpers.enums import ServiceType
from core.services.base.api_key_service_base import ApiKeyServiceBase
from core.services.locator.service_locator import ServicesInjector


class ApiServer:

    def __init__(self, fast_api: FastAPI):
        self.app = fast_api
        self.routers = self.get_routers()
        self.init_api(routers=self.routers)
        self.include_routers(routers=self.routers)
        self.setup_exception_handlers()

    # pylint: disable=unused-argument
    def setup_exception_handlers(self):
        @self.app.exception_handler(HTTPException)
        async def http_exception_handler(request: Request, exc: HTTPException):
            error_response = HttpErrorResponseModel(
                code=exc.status_code,
                detail=exc.detail,
            )
            return JSONResponse(
                content=error_response.model_dump(),
                status_code=exc.status_code,
            )

    def verify_api_key(
        self,
        credentials: HTTPAuthorizationCredentials = Security(HTTPBearer()),
    ) -> None:
        token = credentials.credentials
        if token != os.getenv("API_KEY"):
            raise HTTPException(status_code=401, detail="Invalid or missing API key")

    def get_routers(self) -> RootRouterModel:
        # private endpoints - use dependencies=[Depends(self.verify_api_key)] in APIRouter
        ### users router
        users_router: APIRouter = APIRouter(
            prefix="/users", dependencies=[Depends(self.verify_api_key)]
        )

        # public endpoints
        ### api key router
        api_key: APIRouter = APIRouter(
            prefix="/keys",
        )

        return RootRouterModel(
            users=users_router,
            api_key=api_key,
        )

    def include_routers(self, routers: RootRouterModel) -> None:
        self.app.include_router(router=routers.users)
        self.app.include_router(router=routers.api_key)

    def init_api(self, routers: RootRouterModel) -> None:
        injector_prod = ServicesInjector.injector(ServiceType.PROD)

        UsersAPI(router=routers.users)
        ApiKeyApi(
            router=routers.api_key, api_key_service=injector_prod.get(ApiKeyServiceBase)
        )
