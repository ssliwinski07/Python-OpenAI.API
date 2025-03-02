from pydantic import BaseModel


class ApiKeyModel(BaseModel):
    api_key: str
