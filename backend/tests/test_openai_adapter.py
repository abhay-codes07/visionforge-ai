from app.integrations.openai_vision_client import OpenAIVisionClient


def test_build_content_uses_input_image_for_image_media() -> None:
    content = OpenAIVisionClient._build_content(
        media_type="image",
        prompt="Describe scene",
        source_uri="https://example.com/frame.jpg",
    )
    assert content[0]["type"] == "input_text"
    assert content[1]["type"] == "input_image"


def test_build_content_uses_uri_hint_for_video_media() -> None:
    content = OpenAIVisionClient._build_content(
        media_type="video",
        prompt="Analyze motion",
        source_uri="https://example.com/video.mp4",
    )
    assert content[1]["type"] == "input_text"
    assert "Video source URI" in content[1]["text"]
