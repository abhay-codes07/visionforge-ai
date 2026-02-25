from fastapi import WebSocket

from app.schemas.realtime import RealtimeOutboundMessage


class RealtimeConnectionManager:
    def __init__(self) -> None:
        self._connections: set[WebSocket] = set()

    async def connect(self, websocket: WebSocket) -> None:
        await websocket.accept()
        self._connections.add(websocket)

    def disconnect(self, websocket: WebSocket) -> None:
        self._connections.discard(websocket)

    async def send_message(self, websocket: WebSocket, payload: RealtimeOutboundMessage) -> None:
        await websocket.send_json(payload.model_dump(mode="json"))

    async def broadcast(self, payload: RealtimeOutboundMessage) -> None:
        for websocket in list(self._connections):
            await self.send_message(websocket, payload)
