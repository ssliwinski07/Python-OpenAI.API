from dataclasses import dataclass
from fastapi import APIRouter


@dataclass
class PublicRoutesModel:
    api_key: APIRouter
