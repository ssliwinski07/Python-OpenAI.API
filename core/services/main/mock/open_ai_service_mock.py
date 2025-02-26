from injector import singleton

from openai.types.chat.chat_completion import Choice
from core.services.base.open_ai_service_base import OpenAiServiceBase
from utils.models.open_ai.open_ai_send_message_model import OpenAISendMessageModel


@singleton
class OpenAiServiceMock(OpenAiServiceBase):

    # mock method - for now no need to pass anything
    async def send_message(
        self, open_ai_send_message_model: OpenAISendMessageModel, api_key: str
    ) -> list[Choice]:
        pass
