from abc import ABC, abstractmethod
from typing import Optional


class UsersServiceBase(ABC):
    @abstractmethod
    def get_user(self, user_id: int, user_name: Optional[bool] = None):
        pass
