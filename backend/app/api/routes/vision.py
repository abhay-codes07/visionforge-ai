from fastapi import APIRouter, Depends

from app.api.deps import get_vision_service
from app.schemas.vision import (
    VisionAnalyzeRequest,
    VisionAnalyzeResponse,
    VisionQuestionRequest,
    VisionQuestionResponse,
)
from app.services.vision_service import VisionService

router = APIRouter(prefix="/vision")


@router.post("/analyze", response_model=VisionAnalyzeResponse)
async def analyze_vision(
    payload: VisionAnalyzeRequest,
    service: VisionService = Depends(get_vision_service),
) -> VisionAnalyzeResponse:
    return await service.analyze(payload)


@router.post("/question", response_model=VisionQuestionResponse)
async def ask_vision_question(
    payload: VisionQuestionRequest,
    service: VisionService = Depends(get_vision_service),
) -> VisionQuestionResponse:
    return await service.answer_question(payload)
