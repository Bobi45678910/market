from enum import Enum

from apps.chat.models.ChatModel import Chat
from apps.chat.models.MessageModel import Message


class Models(Enum):
    chat = Chat
    massage = Message
