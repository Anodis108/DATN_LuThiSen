from __future__ import annotations

from common.bases import BaseModel


class CardAlignSettings(BaseModel):
    baseImg_path: str = 'common/weights/detect_cccd_best.pt'
    per_match: float
