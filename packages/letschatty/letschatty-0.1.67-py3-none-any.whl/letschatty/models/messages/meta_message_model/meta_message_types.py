from pydantic import BaseModel
from typing import List, Dict, Union, Optional, TypeAlias

# Mensajes Clasicos
class MetaTextContent(BaseModel):
    body: str

class MetaImageContent(BaseModel):
    caption: Optional[str] = None
    mime_type: str
    sha256: str
    id: str

class MetaStickerContent(BaseModel):
    mime_type: str
    sha256: str
    id: str
    animated: bool

class MetaAudioContent(BaseModel):
    mime_type: str
    sha256: str
    id: str
    voice: bool

class MetaVideoContent(BaseModel):
    caption: Optional[str] = None
    mime_type: str
    sha256: str
    id: str

class MetaDocumentContent(BaseModel):
    caption: str
    filename: str
    mime_type: str
    sha256: str
    id: str

class MetaLocationContent(BaseModel):
    latitude: float
    longitude: float

    address: str = None
    url: str = None
    name: str = None

    def is_location_fixed(self) -> bool:
        return bool(self.address and self.url and self.name)
    
    def is_location_shared(self) -> bool:
        return bool(not self.address and not self.url and not self.name)

# Mensajes de contactos
class Name(BaseModel):
    formatted_name: str
    first_name: str

class Phones(BaseModel):
    phone: str
    wa_id: str
    type: str

class Address(BaseModel):
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None
    country: Optional[str] = None
    country_code: Optional[str] = None
    type: Optional[str] = None

class Email(BaseModel):
    email: str
    type: Optional[str] = None

class FullName(BaseModel):
    formatted_name: str # Full name
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    suffix: Optional[str] = None
    prefix: Optional[str] = None

class Organization(BaseModel):
    company: Optional[str] = None
    department: Optional[str] = None
    title: Optional[str] = None

class Phone(BaseModel):
    phone: str
    type: Optional[str] = None
    wa_id: Optional[str] = None

class Url(BaseModel):
    url: str
    type: Optional[str] = None

class MetaContactContent(BaseModel):
    name: FullName
    phones: Optional[List[Phone]] = None
    addresses: Optional[List[Address]] = None
    birthday: Optional[str] = None
    emails: Optional[List[Email]] = None
    org: Optional[Organization] = None
    urls: Optional[List[Url]] = None
    
    @property
    def phone_number(self) -> Optional[str]:
        """Returns the first phone number that has a valid wa_id"""
        return next((phone.wa_id for phone in self.phones if phone.wa_id), None)
    
    @property
    def full_name(self) -> str:
        """Returns the full name of the contact"""
        return self.name.formatted_name
    
# Mensajes de errores
class ErrorData(BaseModel):
    details: str

class MetaErrorContent(BaseModel):
    code: int
    title: str
    message: str
    error_data: ErrorData

# Mensajse interactivos
class ButtonReply(BaseModel):
    id: str
    title: str

class MetaInteractiveContent(BaseModel):
    button_reply: ButtonReply
    type: str

# Alias
MetaContent : TypeAlias = Union[MetaVideoContent, MetaImageContent, MetaDocumentContent, MetaAudioContent, MetaStickerContent, MetaTextContent, MetaContactContent]