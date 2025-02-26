from typing import Sequence, Optional
from fastapi import APIRouter, Depends

from utils.models.routes.private_routes_model import PrivateRoutesModel
from utils.models.routes.public_routes_model import PublicRoutesModel


class RoutesContainer:

    @classmethod
    def private_routes(cls, dependencies: Sequence[Depends]) -> PrivateRoutesModel:
        users_router: APIRouter = APIRouter(prefix="/users", dependencies=dependencies)
        open_ai_router: APIRouter = APIRouter(
            prefix="/openai", dependencies=dependencies
        )
        return PrivateRoutesModel(users=users_router, open_ai=open_ai_router)

    @classmethod
    def public_routes(
        cls, dependencies: Optional[Sequence[Depends]] = None
    ) -> PublicRoutesModel:
        api_key_router: APIRouter = APIRouter(
            prefix="/keys",
            dependencies=dependencies,
        )
        return PublicRoutesModel(api_key=api_key_router)
