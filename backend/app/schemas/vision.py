from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

MediaType = Literal["image", "video", "webcam"]


class VisionAnalyzeRequest(BaseModel):
    media_type: MediaType
    prompt: str = Field(default="Describe the visual scene and key objects.")
    source_uri: str | None = Field(default=None, description="Optional URI to uploaded media.")


class VisionDetection(BaseModel):
    label: str
    confidence: float = Field(ge=0.0, le=1.0)
    description: str


class VisionAnalyzeResponse(BaseModel):
    request_id: str
    media_type: MediaType
    summary: str
    detections: list[VisionDetection]
    generated_at: datetime


class VisionQuestionRequest(BaseModel):
    request_id: str
    question: str


class VisionQuestionResponse(BaseModel):
    request_id: str
    answer: str
    generated_at: datetime
