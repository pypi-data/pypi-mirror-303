from pydantic import BaseModel, Field
from .content_media import ChattyContentMedia

class ChattyContentDocument(ChattyContentMedia):
    filename: str = Field(description="Name of the document")


    