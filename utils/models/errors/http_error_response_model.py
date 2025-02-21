from pydantic import BaseModel


class HttpErrorResponseModel(BaseModel):
    code: int
    detail: str
