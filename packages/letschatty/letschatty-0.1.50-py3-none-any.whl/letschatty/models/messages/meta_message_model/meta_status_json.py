from __future__ import annotations
from datetime import datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

from .meta_base_notification_json import BaseMetaNotificationJson, Entry, Metadata

from enum import Enum

class StatusType(Enum):
    READ = "read"
    DELIVERED = "delivered"
    SENT = "sent"
    WAITING = "waiting"

class Origin(BaseModel):
    type: str

class Conversation(BaseModel):
    id: str
    origin: Origin

    # Esta propiedad es unica de una conversation tipo sent
    expiration_timestamp: Optional[str] = None

class Pricing(BaseModel):
    billable: bool
    pricing_model: str
    category: str
    
class Status(BaseModel):
    id: str
    status: str  # Aquí el status es un simple string
    timestamp: str
    recipient_id: str
    
    # Un estado de lectura no tiene estas propiedades
    conversation: Optional[Conversation] = None
    pricing: Optional[Pricing] = None

    def is_read(self) -> bool:
        return self.status == StatusType.read.value
    
class Value(BaseModel):
    messaging_product: str
    metadata: Metadata
    statuses: List[Status]

class MetaStatusJson(BaseMetaNotificationJson):
    
    entry: List[Entry] = Field(..., description="List of entries in the notification")
    
    def get_value(self) -> Value:
        print(f"Isntanciando el value el value {self.entry[0].changes[0].value} ")
        return Value(**self.entry[0].changes[0].value)

    def get_status(self) -> Status:
        return self.get_value().statuses[0]

    def get_status_id(self) -> str:
        return self.get_status().id

    def get_status_time(self) -> datetime:
        timestamp = int(self.get_status().timestamp)
        return datetime.fromtimestamp(timestamp)

    def get_status_type(self) -> str:
        return self.get_status().status

    def get_recipient_id(self) -> str:
        return self.get_status().recipient_id

    def get_conversation(self) -> Optional[Dict[str, Any]]:
        return self.get_status().conversation

    def get_pricing(self) -> Optional[Dict[str, Any]]:
        return self.get_status().pricing

    def get_metadata(self) -> Metadata:
        "Obteniendo la metada con el value"
        return self.get_value().metadata
    
    def get_phone_number_id(self) -> str:
        print("Obteniendo la metadata")
        return self.get_metadata().phone_number_id
