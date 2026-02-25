import asyncio
from dataclasses import dataclass
from typing import Literal

from openai import AsyncOpenAI

from app.core.config import Settings

MediaType = Literal["image", "video", "webcam"]


@dataclass(frozen=True)
class OpenAIVisionResult:
    summary: str


class OpenAIVisionClient:
    def __init__(self, settings: Settings) -> None:
        self._model = settings.openai_model
        self._timeout_seconds = settings.openai_timeout_seconds
        self._max_retries = max(0, settings.openai_max_retries)
        self._retry_backoff_seconds = max(0.0, settings.openai_retry_backoff_seconds)
        self._client = AsyncOpenAI(api_key=settings.openai_api_key)

    async def analyze_media(self, media_type: MediaType, prompt: str, source_uri: str | None = None) -> OpenAIVisionResult:
        content = self._build_content(media_type=media_type, prompt=prompt, source_uri=source_uri)

        response = await self._call_with_retry(media_type=media_type, content=content)
        summary = (getattr(response, "output_text", "") or "").strip()
        return OpenAIVisionResult(summary=summary or "No summary returned by model.")

    @staticmethod
    def _build_content(media_type: MediaType, prompt: str, source_uri: str | None) -> list[dict[str, str]]:
        content: list[dict[str, str]] = [{"type": "input_text", "text": prompt}]
        if not source_uri:
            return content

        if media_type == "video":
            content.append({"type": "input_text", "text": f"Video source URI: {source_uri}"})
        else:
            content.append({"type": "input_image", "image_url": source_uri})
        return content

    async def _call_with_retry(self, media_type: MediaType, content: list[dict[str, str]]):
        last_error: Exception | None = None
        total_attempts = self._max_retries + 1

        for attempt in range(total_attempts):
            try:
                return await asyncio.wait_for(
                    self._client.responses.create(
                        model=self._model,
                        input=[{"role": "user", "content": content}],
                        metadata={"media_type": media_type, "attempt": str(attempt + 1)},
                    ),
                    timeout=self._timeout_seconds,
                )
            except Exception as exc:
                last_error = exc
                if attempt >= self._max_retries:
                    break
                await asyncio.sleep(self._retry_backoff_seconds * (attempt + 1))

        if last_error is not None:
            raise last_error
        raise RuntimeError("OpenAI request failed with unknown error state.")
