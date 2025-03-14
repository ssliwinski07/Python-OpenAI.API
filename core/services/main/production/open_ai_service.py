import threading
import logging
from googletrans import Translator
import openai
from openai.types.chat import ChatCompletion, ChatCompletionUserMessageParam
from openai.types.chat.chat_completion import Choice
from injector import singleton

from utils.helpers.consts import USER_ROLE, DEFAULT_ERROR_CODE
from utils.helpers.openai_errors import OPEN_AI_ERRORS
from core.data.models.open_ai.open_ai_send_message_model import OpenAISendMessageModel
from core.exceptions.custom_exception.custom_exception import CustomException
from core.services.base.open_ai_service_base import OpenAiServiceBase
from core.localization.localizations import Localizations


@singleton
class OpenAiService(OpenAiServiceBase):

    def __init__(self):
        self.__openai_client: openai.OpenAI = None
        self.__lock = threading.Lock()
        self.translator = Translator()
        self.lang_code = Localizations.language_code()

    def __initialize_openai_client(self, api_key: str, url: str):
        self.__openai_client: openai.OpenAI = openai.OpenAI(
            api_key=api_key,
            base_url=url,
        )

    async def send_message(
        self, open_ai_send_message_model: OpenAISendMessageModel, api_key: str
    ) -> list[Choice]:

        try:
            with self.__lock:
                # since openAI API is stateless it can be initialized at every HTTP request
                # so no need to initialize it once and use the same client in all methods
                self.__initialize_openai_client(
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

            error_msg: str = e.message if hasattr(e, "message") else str(e)
            error_status_code: int = (
                e.status_code if hasattr(e, "status_code") else DEFAULT_ERROR_CODE
            )

            # added googletrans package to translate errors from openAI, since they are not localized
            if self.lang_code != "en":
                try:
                    async with self.translator:
                        translated_error_msg: str = await self.translator.translate(
                            error_msg, dest=self.lang_code
                        )
                        error_msg = translated_error_msg.text
                except ValueError as translation_exception:
                    logging.error("Translation failed: %s", translation_exception)

            raise CustomException(
                message=error_msg, status_code=error_status_code
            ) from e

        except Exception as e:
            raise CustomException(message=str(e), status_code=DEFAULT_ERROR_CODE) from e
