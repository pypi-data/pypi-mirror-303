from .base.message_base import Message
from ...utils.types.message_types import MessageType

class UnsupportedMessage(Message):
    type: str = MessageType.UNSUPPORTED