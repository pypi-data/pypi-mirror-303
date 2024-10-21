from pydantic import BaseModel, ValidationError

from typing import List, Dict, Optional, Any
from datetime import datetime

from ...utils.types.message_types import MessageType
from ..chatty_messages.schema import ChattyContent, ChattyContext

class rMessageContext(ChattyContext):
    pass

class MessageRequest(BaseModel):
    type: MessageType
    content: ChattyContent
    context: rMessageContext
    date: datetime
    sent_by: Optional[str]

class MessagesRequest(BaseModel):
    agent_email: str
    chat_id: str
    messages: List[MessageRequest]