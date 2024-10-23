from __future__ import annotations
from pydantic import BaseModel, Field, ConfigDict
from typing import List
from datetime import datetime
from ....messages.chatty_messages import MessageRequest

class ChattyResponse(BaseModel):
    id: str = Field(alias="_id")
    updated_at: datetime
    messages: List[MessageRequest]
    
    model_config = ConfigDict(
        populate_by_name=True
    )