# Tipos de mensajes disponibles
from enum import StrEnum

class MessageType(StrEnum):
    TEXT = "text"
    IMAGE = "image"
    VIDEO = "video"
    DOCUMENT = "document"
    STICKER = "sticker"
    AUDIO = "audio"
    REACTION="reaction"
    CENTRAL="central"
    CONTACT = "contacts"
    LOCATION = "location"
    UNSUPPORTED = "unsupported"
    INTERACTIVE = "interactive"
    
class MessageSubtype(StrEnum):
    TEMPLATE = "template"
    CHATTY_RESPONSE = "chatty_response"
    NONE = ""