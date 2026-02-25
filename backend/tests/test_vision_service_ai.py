import pytest

from app.core.config import Settings
from app.core.errors import ServiceUnavailableError
from app.schemas.vision import VisionAnalyzeRequest
from app.services.vision_service import VisionService


class _StubOpenAIClient:
    def __init__(self, summary: str = "AI summary", raises: Exception | None = None) -> None:
        self._summary = summary
        self._raises = raises

    async def analyze_media(self, media_type: str, prompt: str, source_uri: str | None = None):
        if self._raises is not None:
            raise self._raises
        return type("Result", (), {"summary": self._summary})()


@pytest.mark.anyio
async def test_analyze_uses_openai_summary_when_available() -> None:
    settings = Settings(openai_enabled=True, openai_fallback_to_stub=True)
    service = VisionService(openai_client=_StubOpenAIClient(summary="AI-derived scene summary"), settings=settings)

    result = await service.analyze(VisionAnalyzeRequest(media_type="image", prompt="Describe scene"))

    assert result.summary == "AI-derived scene summary"


@pytest.mark.anyio
async def test_analyze_falls_back_to_stub_when_provider_fails_and_fallback_enabled() -> None:
    settings = Settings(openai_enabled=True, openai_fallback_to_stub=True)
    service = VisionService(openai_client=_StubOpenAIClient(raises=RuntimeError("provider down")), settings=settings)

    result = await service.analyze(VisionAnalyzeRequest(media_type="image", prompt="Fallback prompt"))

    assert "Processed image input" in result.summary


@pytest.mark.anyio
async def test_analyze_raises_when_provider_fails_and_fallback_disabled() -> None:
    settings = Settings(openai_enabled=True, openai_fallback_to_stub=False)
    service = VisionService(openai_client=_StubOpenAIClient(raises=RuntimeError("provider down")), settings=settings)

    with pytest.raises(ServiceUnavailableError):
        await service.analyze(VisionAnalyzeRequest(media_type="image", prompt="No fallback prompt"))
