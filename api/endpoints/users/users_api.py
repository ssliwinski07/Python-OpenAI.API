from typing import Optional
from fastapi import APIRouter, HTTPException

from core.data.models.users.user_model import User
from core.localization.localizations import Localizations
from utils.messages import messages


class UsersAPI:
    def __init__(self, router: APIRouter):
        self.router = router
        self.routes_setup()

    def routes_setup(self):
        # test method to show how function verify_api_key from ApiServer works
        # user_name: Optional[bool] used only to see optional query parameter in swagger api docs
        @self.router.get("/{user_id}", tags=["Users"])
        def get_user(user_id: int, user_name: Optional[bool] = None) -> User:
            if user_id != 1:
                raise HTTPException(
                    status_code=404,
                    detail=Localizations.translate(msg=messages.USER_NOT_FOUND),
                )
            return User(name="John", lastname="Doe", age=25)
