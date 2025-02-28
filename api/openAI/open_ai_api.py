from fastapi import APIRouter, HTTPException, Request
from openai.types.chat.chat_completion import Choice

from utils.models.open_ai.open_ai_send_message_model import OpenAISendMessageModel
from utils.helpers.consts import DEFAULT_ERROR_CODE
from core.exceptions.custom_exception.custom_exception import CustomException
from core.services.base.open_ai_service_base import OpenAiServiceBase


class OpenAIAPI:

    def __init__(self, router: APIRouter, open_ai_service: OpenAiServiceBase):
        self.router = router
        self.open_ai_service = open_ai_service
        self.routes_setup()

    def routes_setup(self):
        @self.router.post("/", tags=["OpenAI"])
        async def send_message(
            open_ai_send_message_model: OpenAISendMessageModel, request: Request
        ) -> list[Choice]:
            try:
                auth_header: str = request.headers.get("Authorization")
                api_key: str = auth_header.split(" ")[1]

                return await self.open_ai_service.send_message(
                    open_ai_send_message_model=open_ai_send_message_model,
                    api_key=api_key,
                )

            except CustomException as e:
                raise HTTPException(status_code=e.status_code, detail=e.message) from e

            except Exception as e:
                raise HTTPException(
                    status_code=DEFAULT_ERROR_CODE, detail=str(e)
                ) from e
