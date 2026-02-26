from fastapi.testclient import TestClient

from app.main import app


def test_live_session_snapshot_endpoint() -> None:
    client = TestClient(app)
    response = client.get("/api/v1/live/sessions/demo-session")
    assert response.status_code == 200
    payload = response.json()
    assert payload["session_id"] == "demo-session"
    assert isinstance(payload["detection_count"], int)


def test_live_question_endpoint() -> None:
    client = TestClient(app)
    response = client.post(
        "/api/v1/live/question",
        json={"session_id": "demo-session", "question": "What is happening?", "demo_mode": "workspace"},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["session_id"] == "demo-session"
    assert isinstance(payload["answer"], str)


def test_live_websocket_question_stream() -> None:
    client = TestClient(app)
    with client.websocket_connect("/api/v1/ws/live") as ws:
        _ = ws.receive_json()
        ws.send_json({"type": "question", "session_id": "demo-session", "question": "Any person detected?"})
        event = ws.receive_json()
        assert event["type"] in {"token", "error"}
