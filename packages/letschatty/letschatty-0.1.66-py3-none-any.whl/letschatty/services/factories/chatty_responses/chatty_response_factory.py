from __future__ import annotations
from pydantic import BaseModel, Field
from typing import List, Dict, Any
from datetime import datetime
from zoneinfo import ZoneInfo
from bson import ObjectId
from ....models.messages.chatty_messages import MessageRequest
from ....models.company.assets import ChattyResponse
from ....models.messages.chatty_messages.schema import ChattyContext
from ....models.utils import MessageSubtype

class ChattyResponseFactory:
    @staticmethod
    def create(messages: List[Dict[str, Any]]) -> ChattyResponse:
        """This method is used to create a ChattyResponse from a JSON object"""
        id = str(ObjectId())
        updated_at = datetime.now(tz=ZoneInfo("UTC"))
        chatty_context = ChattyContext(response_id=id)
        subtype = MessageSubtype.CHATTY_RESPONSE
        messages = [MessageRequest.from_response(data=message, context=chatty_context, subtype=subtype) for message in messages]
        return ChattyResponse(id=id, updated_at=updated_at, messages=messages)
    
    @staticmethod
    def update(chatty_response: ChattyResponse, messages: List[Dict[str, Any]]) -> ChattyResponse:
        """This method is used to update a ChattyResponse with a new list of messages"""
        chatty_context = ChattyContext(response_id=chatty_response.id)
        subtype = MessageSubtype.CHATTY_RESPONSE
        messages = [MessageRequest.from_response(data=message, context=chatty_context, subtype=subtype) for message in messages]
        chatty_response.updated_at = datetime.now(tz=ZoneInfo("UTC"))
        chatty_response.messages = messages
        return chatty_response