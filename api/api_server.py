import os
from fastapi import FastAPI, HTTPException, Request, Depends, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from api.initializer.api_initializer import ApiInitializer
from api.routes.routes_container import RoutesContainer
from utils.models.errors.http_error_response_model import HttpErrorResponseModel
from utils.models.routes.private_routes_model import PrivateRoutesModel
from utils.models.routes.public_routes_model import PublicRoutesModel
from utils.models.routes.routes_container_model import RoutesContainerModel
from utils.messages import messages
from core.localization.localizations import Localizations
from core.services.locator.services_injector import ServicesInjector


class ApiServer:

    def __init__(self, services_injector: ServicesInjector, fast_api: FastAPI):
        self.app = fast_api
        self.services_injector = services_injector
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
            raise HTTPException(
                status_code=401,
                detail=Localizations.translate(msg=messages.INVALID_OR_MISSING_API_KEY),
            )

    def get_routers(self) -> RoutesContainerModel:

        private: PrivateRoutesModel = RoutesContainer.private_routes(
            dependencies=[Depends(self.verify_api_key)]
        )
        public: PublicRoutesModel = RoutesContainer.public_routes()

        return RoutesContainerModel(private=private, public=public)

    def include_routers(self, routers: RoutesContainerModel) -> None:

        for _, router in routers.private.__dict__.items():
            if isinstance(router, APIRouter):
                self.app.include_router(router=router)

        for _, router in routers.public.__dict__.items():
            if isinstance(router, APIRouter):
                self.app.include_router(router=router)

    def init_api(self, routers: RoutesContainerModel) -> None:
        ApiInitializer(
            routers=routers, services_injector=self.services_injector
        ).initialize()
