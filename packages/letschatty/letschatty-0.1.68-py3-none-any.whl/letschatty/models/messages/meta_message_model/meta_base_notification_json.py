from pydantic import BaseModel, Field
from typing import List, Any, Dict
from enum import StrEnum
from .value_messages import Message
# from .meta_status_json import Status
# from .meta_error_json import Error

class NotificationType(StrEnum):
    MESSAGES = "messages"
    STATUSES = "statuses"
    ERRORS = "errors"  
    UNKNOWN = "unknown"
    INEXISTENT = "inexistent"
    
class Metadata(BaseModel):
    display_phone_number: str
    phone_number_id: str


class Profile(BaseModel):
    name: str

class Contact(BaseModel):
    profile: Profile
    wa_id: str

class Value(BaseModel):
    messaging_product: str
    metadata: Metadata
    contacts: List[Contact] = Field(default_factory= lambda: [])
    messages: List[Message] = Field(default_factory= lambda: [])
    statuses: List[Dict[str, Any]] = Field(default_factory= lambda: [])
    errors: List[Dict[str, Any]] = Field(default_factory= lambda: [])

    def is_messages(self) -> bool:
        return bool(self.contacts != [] and self.messages != [])

    def is_statuses(self) -> bool:
        return bool(self.statuses != [])
    
    def is_errors(self) -> bool:
        return bool(self.errors != [])
    
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
        
    
    def get_value(self) -> Value:
        return self.entry[0].changes[0].value