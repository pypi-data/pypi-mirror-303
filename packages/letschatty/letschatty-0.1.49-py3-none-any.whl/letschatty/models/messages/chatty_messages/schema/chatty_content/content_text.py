from pydantic import BaseModel

class ChattyContentText(BaseModel):
    body: str 
    preview_url: bool = False