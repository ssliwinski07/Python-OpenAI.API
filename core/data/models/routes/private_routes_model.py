from dataclasses import dataclass
from fastapi import APIRouter


@dataclass
class PrivateRoutesModel:
    users: APIRouter
    open_ai: APIRouter
