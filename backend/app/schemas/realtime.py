from datetime import datetime
from typing import Literal

from pydantic import BaseModel

RealtimeEventType = Literal["connected", "analysis", "token", "error", "completed"]


class RealtimeInboundMessage(BaseModel):
    type: Literal["analyze", "question", "ping"]
    request_id: str | None = None
    prompt: str | None = None
    media_type: Literal["image", "video", "webcam"] | None = None
    question: str | None = None


class RealtimeOutboundMessage(BaseModel):
    type: RealtimeEventType
    request_id: str | None = None
    content: str
    timestamp: datetime
