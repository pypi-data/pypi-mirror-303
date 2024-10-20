from pydantic import BaseModel, Field
from typing import Optional
class ChattyContentMedia(BaseModel):
    id: Optional[str] = Field(description="Unique identifier for the image. Also known as media_id", default="")
    url: str = Field(description="URL of the media from S3")
    caption: str = Field(default="", description="Caption of the media that goes as a text below the media")
    mime_type: str
    sha256: str
