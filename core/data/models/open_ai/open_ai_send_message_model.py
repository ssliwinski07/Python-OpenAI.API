from pydantic import BaseModel


class OpenAISendMessageModel(BaseModel):
    message: str
    model: str
    url: str
