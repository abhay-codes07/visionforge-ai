from __future__ import annotations

import base64
from typing import Any

import cv2
import numpy as np

from app.core.config import Settings, get_settings
from app.schemas.live import BoundingBox, LiveDetection


class YoloService:
    def __init__(self, settings: Settings | None = None) -> None:
        self._settings = settings or get_settings()
        self._model: Any | None = None

    def detect_from_base64(self, image_base64: str) -> list[LiveDetection]:
        frame = self._decode_frame(image_base64)
        if frame is None:
            return []

        model = self._get_model()
        results = model.predict(frame, conf=self._settings.yolo_confidence_threshold, verbose=False)
        if not results:
            return []

        detections: list[LiveDetection] = []
        for row in results[0].boxes:
            xyxy = row.xyxy[0].tolist()
            x1, y1, x2, y2 = xyxy
            cls_index = int(row.cls[0].item())
            label = model.names.get(cls_index, f"class-{cls_index}")
            confidence = float(row.conf[0].item())
            detections.append(
                LiveDetection(
                    label=label,
                    confidence=confidence,
                    box=BoundingBox(x=x1, y=y1, width=max(0.0, x2 - x1), height=max(0.0, y2 - y1)),
                )
            )
        return detections

    def _get_model(self):
        if self._model is None:
            from ultralytics import YOLO

            self._model = YOLO(self._settings.yolo_model)
        return self._model

    @staticmethod
    def _decode_frame(image_base64: str):
        try:
            raw = base64.b64decode(image_base64)
            array = np.frombuffer(raw, dtype=np.uint8)
            return cv2.imdecode(array, cv2.IMREAD_COLOR)
        except Exception:
            return None
