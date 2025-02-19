from fastapi import FastAPI, APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

from core.api.routers.users.users_api import UsersAPI
from core.api.routers.tokens.open_ai_token_api import OpenAITokenAPI
from utils.models.routers.root.root_router import RootRouter
from utils.models.errors.http_error_response import HttpErrorResponse


class ApiServer:

    def __init__(self, fast_api: FastAPI):
        self.app = fast_api
        self.routers = self.get_routers()
        self.init_api(routers=self.routers)
        self.include_routers(routers=self.routers)
        self.setup_exception_handlers()

    def setup_exception_handlers(self):
        @self.app.exception_handler(HTTPException)
        async def http_exception_handler(request: Request, exc: HTTPException):
            error_response = HttpErrorResponse(code=exc.status_code, detail=exc.detail)
            return JSONResponse(
                content=error_response.model_dump(),
                status_code=exc.status_code,
            )

    def get_routers(self) -> RootRouter:
        # users router
        users_router: APIRouter = APIRouter(prefix="/users")

        # acces token
        api_key: APIRouter = APIRouter(prefix="/keys")

        return RootRouter(
            users=users_router,
            api_key=api_key,
        )

    def include_routers(self, routers: RootRouter) -> None:
        self.app.include_router(router=routers.users)
        self.app.include_router(router=routers.api_key)

    def init_api(self, routers: RootRouter) -> None:
        UsersAPI(router=routers.users)
        OpenAITokenAPI(router=routers.api_key)
