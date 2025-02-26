import openai
from openai.types.chat import ChatCompletion, ChatCompletionUserMessageParam
from openai.types.chat.chat_completion import Choice
from injector import singleton

from utils.helpers.consts import USER_ROLE
from utils.helpers.openai_errors import OPEN_AI_ERRORS
from utils.models.open_ai.open_ai_send_message_model import OpenAISendMessageModel
from core.exceptions.custom_exception.custom_exception import CustomException
from core.services.base.open_ai_service_base import OpenAiServiceBase


@singleton
class OpenAiService(OpenAiServiceBase):

    def __init__(self):
        self.__openai_client: openai.OpenAI = None

    def __initialize_openai_client(self, api_key: str, url: str):

        self.__openai_client: openai.OpenAI = openai.OpenAI(
            api_key=api_key,
            base_url=url,
        )

        if not self.__openai_client:
            raise ValueError("TEST_TEST_TEST")

        return self.__openai_client

    async def send_message(
        self, open_ai_send_message_model: OpenAISendMessageModel, api_key: str
    ) -> list[Choice]:

        try:
            if not self.__openai_client:
                self.__openai_client = self.__initialize_openai_client(
                    api_key=api_key,
                    url=open_ai_send_message_model.url,
                )

            messages = [
                ChatCompletionUserMessageParam(
                    role=USER_ROLE, content=open_ai_send_message_model.message
                )
            ]

            response: ChatCompletion = (
                await self.__openai_client.chat.completions.create(
                    model=open_ai_send_message_model.model, messages=messages
                )
            )

            return response.choices

        except OPEN_AI_ERRORS as e:
            error_body = getattr(e, "body", str(e))
            error_status_code = getattr(e, "status_code", "-")

            error_msg = (
                f"Error message: {error_body['message']}. "
                f"Error code: {error_body['code']} ({error_status_code})"
                if "message" in error_body and "code" in error_body
                else str(e)
            )

            raise CustomException(
                message=error_msg, status_code=error_status_code
            ) from e

        except Exception as e:
            raise CustomException(message=str(e), status_code=400) from e
