from .base.message_base import Message
from ...utils.types.message_types import MessageType

class UnknownMessage(Message):
    #TODO: Implementar
    type: str = MessageType.UNSUPPORTED