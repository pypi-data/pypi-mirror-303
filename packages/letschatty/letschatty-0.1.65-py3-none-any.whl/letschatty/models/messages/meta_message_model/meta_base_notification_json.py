from pydantic import BaseModel, Field
from typing import List, Any, Dict
from enum import StrEnum

class NotificationType(StrEnum):
    MESSAGES = "messages"
    STATUSES = "statuses"
    ERRORS = "errors"  
    UNKNOWN = "unknown"
    INEXISTENT = "inexistent"
    
class Metadata(BaseModel):
    display_phone_number: str
    phone_number_id: str

class Value(BaseModel):
    messaging_product: str
    metadata: Metadata
    contacts: List[Dict[str, Any]] = Field(default_factory=list)
    messages: List[Dict[str, Any]] = Field(default_factory=list)
    statuses: List[Dict[str, Any]] = Field(default_factory=list)
    errors: List[Dict[str, Any]] = Field(default_factory=list)

    def is_messages(self) -> bool:
        return bool(self.contacts != [] and self.messages != [])

    def is_statuses(self) -> bool:
        return bool(self.statuses != [])
    
    def is_errors(self) -> bool:
        return bool(self.errors != [])

class Contact(BaseModel):
    profile: Dict[str, str]
    wa_id: str

class Change(BaseModel):
    value: Value
    field: str

class Entry(BaseModel):
    id: str
    changes: List[Change]

class BaseMetaNotificationJson(BaseModel):
    object: str
    entry: List[Entry]

    def get_notification_type(self) -> NotificationType: 
    
        try: 
            value = self.entry[0].changes[0].value

            if value.is_messages():
                return NotificationType.MESSAGES
            elif value.is_statuses():
                return NotificationType.STATUSES
            elif value.is_errors():
                return NotificationType.ERRORS
            else:
                return NotificationType.UNKNOWN
                
        except ValueError:
            return NotificationType.INEXISTENT