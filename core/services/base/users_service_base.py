from abc import ABC, abstractmethod
from typing import Optional

from utils.models.users.user_model import User


class UsersServiceBase(ABC):

    @abstractmethod
    def get_user(self, user_id: int, user_name: Optional[bool] = None) -> User:
        pass
