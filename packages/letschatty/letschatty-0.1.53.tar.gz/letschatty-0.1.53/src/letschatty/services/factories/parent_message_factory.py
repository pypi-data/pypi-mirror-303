# Fabrica principal de mensajes, que convierte mensajes de meta, frontend o BD a mensajes de Chatty
from __future__ import annotations
from typing import TYPE_CHECKING, Dict, Any
from bson import ObjectId
from datetime import datetime
from zoneinfo import ZoneInfo
from .child_db_message_factory import JsonMessageFactory
from .child_request_message import MessagefromMessageRequestFactory
from ...models.messages import ChattyMessageJson, CentralNotification
from ...models.messages.chatty_messages.schema import ChattyContentCentral
from ...models.utils import MessageType, Status

if TYPE_CHECKING:
    from ...models.messages import ChattyMessage, MessageRequest

def from_message_json(message_json : Dict[str, Any]) -> ChattyMessage | None:
    chatty_message_json = ChattyMessageJson(**message_json)
    return JsonMessageFactory.from_db(chatty_message_json)
    
def from_message_request(message_request : MessageRequest) -> ChattyMessage | None:
    return MessagefromMessageRequestFactory.from_frontend(message_request)
  
def from_notification_body(notification_body: str) -> CentralNotification:
    return CentralNotification(
        created_at=datetime.now(tz=ZoneInfo("UTC")),
        updated_at=datetime.now(tz=ZoneInfo("UTC")),
        type=MessageType.CENTRAL,
        content=ChattyContentCentral(body=notification_body),
        status=Status.DELIVERED,
        is_incoming_message=False,
        id=str(ObjectId()),
        sent_by="notifications@letschatty.com",
        starred=False)