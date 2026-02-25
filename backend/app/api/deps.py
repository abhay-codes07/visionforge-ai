from app.services.vision_service import VisionService


def get_vision_service() -> VisionService:
    return VisionService()
