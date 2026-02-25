from functools import lru_cache

from app.core.config import get_settings
from app.integrations.openai_vision_client import OpenAIVisionClient
from app.services.vision_service import VisionService


def get_vision_service() -> VisionService:
    return VisionService()


@lru_cache
def get_openai_vision_client() -> OpenAIVisionClient | None:
    settings = get_settings()
    if not settings.openai_enabled:
        return None
    return OpenAIVisionClient(settings=settings)
