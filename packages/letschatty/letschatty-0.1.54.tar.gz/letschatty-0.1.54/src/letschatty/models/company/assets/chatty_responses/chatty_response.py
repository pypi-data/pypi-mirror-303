from __future__ import annotations
from pydantic import BaseModel
from typing import List
from datetime import datetime
from ....messages.chatty_messages import MessageRequest

class ChattyResponse(BaseModel):
    _id: str
    updated_at: datetime
    messages: List[MessageRequest]
    
    @property
    def id(self) -> str:
        return self._id