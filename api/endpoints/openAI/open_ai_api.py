from injector import inject
from fastapi import APIRouter, HTTPException, Request, Depends
from openai.types.chat.chat_completion import Choice

from core.data.models.open_ai.open_ai_send_message_model import OpenAISendMessageModel
from core.exceptions.custom_exception.custom_exception import CustomException
from core.services.base.open_ai_service_base import OpenAiServiceBase
from core.services.dependency_injection.services_resolver import ServicesResolver
from utils.helpers.consts import DEFAULT_ERROR_CODE


class OpenAIAPI:

    @inject
    def __init__(self, router: APIRouter):
        self.router = router
        self.routes_setup()

    def get_open_ai_service(self) -> OpenAiServiceBase:
        return ServicesResolver.get_open_ai_service()

    def routes_setup(self):
        @self.router.post("/", tags=["OpenAI"])

        # used dependency injection concept from FastAPI
        async def send_message(
            open_ai_send_message_model: OpenAISendMessageModel,
            request: Request,
            open_ai_service: OpenAiServiceBase = Depends(self.get_open_ai_service),
        ) -> list[Choice]:
            try:
                auth_header: str = request.headers.get("Authorization")
                api_key: str = auth_header.split(" ")[1]

                return await open_ai_service.send_message(
                    open_ai_send_message_model=open_ai_send_message_model,
                    api_key=api_key,
                )

            except CustomException as e:
                raise HTTPException(status_code=e.status_code, detail=e.message) from e

            except Exception as e:
                raise HTTPException(
                    status_code=DEFAULT_ERROR_CODE, detail=str(e)
                ) from e
