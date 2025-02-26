from abc import ABC, abstractmethod
from openai.types.chat.chat_completion import Choice
from utils.models.open_ai.open_ai_send_message_model import OpenAISendMessageModel


class OpenAiServiceBase(ABC):

    @abstractmethod
    async def send_message(
        self, open_ai_send_message_model: OpenAISendMessageModel, api_key: str
    ) -> list[Choice]:
        pass
