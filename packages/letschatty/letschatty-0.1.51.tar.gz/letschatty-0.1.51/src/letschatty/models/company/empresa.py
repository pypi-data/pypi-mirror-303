from pydantic import BaseModel, Field
from typing import Optional

class Empresa(BaseModel):
    name: str
    phone_number_id: str = Field(alias="company_id")
    bussiness_account_id: str
    photo_url: str
    meta_token: str
    slack_channel_id: Optional[str] = Field(default=None)
    phone_numbers_for_testing: list[str] = Field(default=[])