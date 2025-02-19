from pydantic import BaseModel


class HttpErrorResponse(BaseModel):
    code: int
    detail: str
