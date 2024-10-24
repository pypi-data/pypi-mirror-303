from .meta_base_notification_json import BaseMetaNotificationJson
from pydantic import BaseModel
from typing import *

# Existen 2 tipos de errores
# entry.changes.value.errors (Este es el que se va a usar)
# entry.changes.value.messages.errors (Este no se va a usar)

class MetaErrorJson:
    data : Dict[str, Any]
    
class Error(BaseModel):
    pass