from datetime import datetime
from typing import Optional

from pydantic import UUID4, BaseModel


class CreateApiKeyRequest(BaseModel):
    description: str
    expires_at: Optional[datetime] = None


class BaseApiKey(BaseModel):
    id: UUID4
    created_at: datetime
    updated_at: datetime
    last_used: Optional[datetime] = None
    truncated: str


class ApiKeyResponse(BaseApiKey, CreateApiKeyRequest):
    truncated: str


class CreateApiKeyResponse(ApiKeyResponse):
    api_key: str
