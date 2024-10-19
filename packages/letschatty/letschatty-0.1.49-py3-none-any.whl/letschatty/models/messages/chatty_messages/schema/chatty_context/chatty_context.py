from __future__ import annotations
from pydantic import BaseModel
from typing import Optional

from ....meta_message_model.meta_message_json import MetaContext
    
class ChattyContext(BaseModel):
    message_id: str
    template_name: Optional[str] = None
    response_id: Optional[str] = None
    
    def model_dump(self, *args, **kwargs):
        kwargs['exclude_unset'] = True
        return super().model_dump(*args, **kwargs)
    
    @classmethod
    def from_meta(cls, meta_context: MetaContext) -> ChattyContext:
        return cls(message_id=meta_context.id)

    @classmethod
    def default(cls) -> ChattyContext:
        return cls(message_id="")