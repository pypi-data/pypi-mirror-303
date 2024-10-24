from __future__ import annotations
from datetime import datetime
from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel, Field

from .meta_message_types import MetaTextContent, MetaImageContent, MetaStickerContent, MetaAudioContent, MetaVideoContent, MetaDocumentContent, MetaContactContent, MetaLocationContent
from ...utils.types.message_types import MessageType

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
    context: Optional[MetaContext] = None
    referral: Optional[MetaReferral] = None
    text: Optional[MetaTextContent] = None
    image: Optional[MetaImageContent] = None
    audio: Optional[MetaAudioContent] = None
    document: Optional[MetaDocumentContent] = None
    video: Optional[MetaVideoContent] = None
    sticker: Optional[MetaStickerContent] = None
    location: Optional[MetaLocationContent] = None
    contacts: Optional[List[MetaContactContent]] = None
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

