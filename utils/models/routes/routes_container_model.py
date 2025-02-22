from dataclasses import dataclass
from utils.models.routes.private_routes_model import PrivateRoutesModel
from utils.models.routes.public_routes_model import PublicRoutesModel


@dataclass
class RoutesContainerModel:
    private: PrivateRoutesModel
    public: PublicRoutesModel
