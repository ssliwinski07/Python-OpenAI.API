from fastapi import APIRouter


class RootRouterModel:
    def __init__(self, users: APIRouter, api_key: APIRouter):
        self.users = users
        self.api_key = api_key
