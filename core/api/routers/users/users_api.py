from fastapi import APIRouter, HTTPException
from utils.models.users.user_model import User


class UsersAPI:
    def __init__(self, router: APIRouter):
        self.router = router
        self.routes_setup()

    def routes_setup(self):
        @self.router.get("/{user_id}", tags=["Users"])
        def get_user(user_id: int):
            if user_id != 1:
                raise HTTPException(status_code=404, detail="User not found")
            user = User(name="John", lastname="Doe", age=25)
            return user
