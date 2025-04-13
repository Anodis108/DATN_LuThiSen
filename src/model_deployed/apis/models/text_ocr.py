"""Face detector API format input """
from __future__ import annotations

from typing import List

from common.bases import BaseModel

# from typing import Any


class APIInput(BaseModel):
    img: List[List[List[int]]]
    classes: List[str]
    bboxes: List[List[float]]


class APIOutput(BaseModel):
    info: List[OCRResult]


class OCRResult(BaseModel):
    class_name: str
    bounding_box: List[float]
    text: str
