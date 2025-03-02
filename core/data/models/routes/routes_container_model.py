from dataclasses import dataclass
from core.data.models.routes.private_routes_model import PrivateRoutesModel
from core.data.models.routes.public_routes_model import PublicRoutesModel


@dataclass
class RoutesContainerModel:
    private: PrivateRoutesModel
    public: PublicRoutesModel
