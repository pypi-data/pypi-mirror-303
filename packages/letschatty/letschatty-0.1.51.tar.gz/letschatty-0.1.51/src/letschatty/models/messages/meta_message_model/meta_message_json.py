from __future__ import annotations
from datetime import datetime
from typing import List, Optional, Dict, Any, TYPE_CHECKING, Union
from pydantic import BaseModel, Field

from .meta_base_notification_json import BaseMetaNotificationJson, Change, Entry, Metadata, Contact
from .meta_message_types import MetaTextContent, MetaImageContent, MetaStickerContent, MetaAudioContent, MetaVideoContent, MetaDocumentContent, MetaContactContent, MetaLocationContent

# if TYPE_CHECKING:
from ...utils.types.message_types import MessageType

# Buscar ejemplo para el referral
class MetaReferral(BaseModel):
    source_url: str
    source_id: str
    source_type: str
    headline: str
    body: str
    media_type: str
    image_url: Optional[str] = None
    video_url: Optional[str] = None
    thumbnail_url: Optional[str] = None
    ctwa_clid: Optional[str] = None

class ReferredProduct(BaseModel):
    catalog_id: str
    product_retailer_id: str

class MetaContext(BaseModel):
    from_: str = Field(..., alias="from")
    id: str

    referred_product : Optional[ReferredProduct] = None

class Message(BaseModel):
    from_: str = Field(..., alias="from")
    id: str
    timestamp: str
    type: MessageType
    
    # Información adicional de interaccion o anuncio
    context: Optional[MetaContext] = None # Algunos tienen contexto y otros mensajes no
    referral: Optional[MetaReferral] = None # Algunos tienen referral y otros mensajes no
    
    # Tipo de mensaje
    text: Optional[MetaTextContent] = None
    image: Optional[MetaImageContent] = None
    audio: Optional[MetaAudioContent] = None
    document: Optional[MetaDocumentContent] = None
    video: Optional[MetaVideoContent] = None
    sticker: Optional[MetaStickerContent] = None
    location: Optional[MetaLocationContent] = None
    contacts: Optional[MetaContactContent] = None
    unsupported: Optional[Dict[str, Any]] = None

    def get_content(self) -> Optional[Union[MetaTextContent, MetaImageContent, MetaStickerContent, MetaAudioContent, MetaVideoContent, MetaDocumentContent, MetaContactContent]]:
        return getattr(self, self.type.value)

    # Metodos para entender el mensaje en base a context y referral
    def is_response_to_specific_message(self) -> bool:
        """Determina si el mensaje es una respuesta a un mensaje específico anterior"""
        return self.context is not None and self.context.id is not None

    def is_interaction_from_button_or_menu(self) -> bool:
        """Determina si el mensaje proviene de una interacción con un botón o menú"""
        pass
        # return self.context is not None and self.context.interaction_type in ['button_press', 'menu_selection']

    def is_response_to_app_event(self) -> bool:
        """Determina si el mensaje es una respuesta a un evento dentro de una aplicación"""
        pass
        # return self.context is not None and self.context.interaction_type == 'app_event'

    def is_initiated_by_campaign_link(self) -> bool:
        """Determina si el mensaje fue iniciado por un enlace de campaña."""
        return self.referral is not None and 'campaign' in self.referral.source_type

    def is_after_ad_interaction(self) -> bool:
        """Determina si el mensaje fue enviado después de interactuar con un anuncio."""
        return self.referral is not None and 'ad' in self.referral.source_type

    def is_from_web_redirection(self) -> bool:
        """Determina si el mensaje proviene de una redirección web."""
        return self.referral is not None and 'web_redirection' in self.referral.source_type

class Value(BaseModel):
    messaging_product: str
    metadata: Metadata
    contacts: List[Contact]
    messages: List[Message]

class MetaMessageJson(BaseMetaNotificationJson):
    
    entry: List[Entry] = Field(..., description="List of entries in the notification")
    
    def get_value(self) -> Value:
        return self.entry[0].changes[0].value

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
        # Suponiendo que originalmente devuelve un string, nacesitamos convertirlo a MessageType
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