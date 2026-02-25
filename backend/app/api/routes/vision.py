from typing import Literal

from fastapi import APIRouter, Depends, File, Form, UploadFile

from app.api.deps import get_vision_service
from app.core.config import get_settings
from app.schemas.vision import (
    VisionAnalyzeRequest,
    VisionAnalyzeResponse,
    VisionCapabilitiesResponse,
    VisionQuestionRequest,
    VisionQuestionResponse,
    VisionUploadResponse,
)
from app.services.storage_service import StorageService
from app.services.vision_service import VisionService

router = APIRouter(prefix="/vision")
storage_service = StorageService()
settings = get_settings()


@router.post("/analyze", response_model=VisionAnalyzeResponse)
async def analyze_vision(
    payload: VisionAnalyzeRequest,
    service: VisionService = Depends(get_vision_service),
) -> VisionAnalyzeResponse:
    return await service.analyze(payload)


@router.get("/capabilities", response_model=VisionCapabilitiesResponse)
async def get_vision_capabilities() -> VisionCapabilitiesResponse:
    return VisionCapabilitiesResponse(
        supported_media_types=["image", "video", "webcam"],
        supported_transports=["rest", "websocket"],
        supports_streaming=True,
        model=settings.openai_model,
    )


@router.post("/question", response_model=VisionQuestionResponse)
async def ask_vision_question(
    payload: VisionQuestionRequest,
    service: VisionService = Depends(get_vision_service),
) -> VisionQuestionResponse:
    return await service.answer_question(payload)


@router.post("/upload", response_model=VisionUploadResponse)
async def upload_media(
    media_type: Literal["image", "video", "webcam"] = Form(...),
    file: UploadFile = File(...),
) -> VisionUploadResponse:
    return await storage_service.save_upload(file, media_type)
