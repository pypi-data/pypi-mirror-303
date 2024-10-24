from __future__ import annotations
from datetime import datetime
from typing import List, Optional, Dict, Any, TYPE_CHECKING

from .meta_base_notification_json import BaseMetaNotificationJson, Metadata
from .meta_message_types import MetaTextContent, MetaImageContent, MetaStickerContent, MetaAudioContent, MetaVideoContent, MetaDocumentContent, MetaContactContent, MetaLocationContent
from ...utils.types.message_types import MessageType

if TYPE_CHECKING:
    from .value_messages import Message, MetaContext

class MetaMessageJson(BaseMetaNotificationJson):
    pass
    
    def get_message(self) -> Message:
        value = self.get_value()
        if isinstance(value.messages[0], dict):
            # Convertir dict a Message si es necesario
            return Message(**value.messages[0])
        return value.messages[0]

    def get_wa_id(self) -> str:
        return self.get_message().id

    def get_created_at(self) -> datetime:
        timestamp = int(self.get_message().timestamp)
        return datetime.fromtimestamp(timestamp)

    def get_referral(self) -> Optional[Dict[str, Any]]:
        return self.get_message().referral

    def get_type(self) -> MessageType:
        raw_type = self.get_message().type  
        return MessageType(raw_type)
    
    def get_message_content(self) -> MetaTextContent | MetaImageContent | MetaStickerContent | MetaAudioContent | MetaVideoContent | MetaDocumentContent | MetaContactContent:
        return self.get_message().get_content()

    def get_message_content_dict(self) -> dict:
        content = self.get_message_content()
        if content is None:
            return {}  # Retorna un diccionario vacío si el contenido es None
        return dict(content)

    def get_sender_wa_id(self) -> str:
        return self.get_value().contacts[0].wa_id

    def get_metadata(self) -> Metadata:
        return self.get_value().metadata
    
    def get_phone_number_id(self) -> str:
        return self.get_metadata().phone_number_id

    def get_context(self) -> MetaContext:
        return self.get_message().context