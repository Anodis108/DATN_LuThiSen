from __future__ import annotations

from typing import List

import numpy as np
import requests  # type: ignore
from common.bases import BaseModel
from common.bases import BaseService
from common.logs import get_logger
from common.settings import Settings

# from typing import Any
logger = get_logger(__name__)


class TextOCRInput(BaseModel):
    img: np.ndarray  # Ảnh đầu vào
    class_list: List[str]
    bboxes_list: List[List[float]]


class TextOCROutput(BaseModel):
    results: List[dict]


class TextOCR(BaseService):
    settings: Settings

    def process(self, inputs: TextOCRInput) -> TextOCROutput:
        payload = {
            'img': inputs.img.tolist(),  # Chuyển ảnh NumPy sang list
            'class_list': inputs.class_list,  # Danh sách class
            'bboxes_list': inputs.bboxes_list,  # Danh sách tọa độ vùng văn bản
        }
        response = requests.post(
            str(self.settings.host_text_ocr), json=payload,
        )

        return TextOCROutput(pred=response.json()['info'])
