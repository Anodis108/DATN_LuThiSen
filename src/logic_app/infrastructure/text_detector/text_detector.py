from __future__ import annotations

from typing import List

import numpy as np
import requests  # type: ignore
from common.bases import BaseModel
from common.bases import BaseService
from common.settings import Settings

# from io import BytesIO
# import cv2


class TextDetectorInput(BaseModel):
    img_origin: np.ndarray
    bbox: List[int]


class TextDectorOutput(BaseModel):
    class_list: List[str]
    bboxes_list: List[List[float]]
    conf_list: List[float]
    processed_image: np.ndarray


class TextDetector(BaseService):
    settings: Settings

    def process(self, inputs: TextDetectorInput) -> TextDectorOutput:
        payload = {
            'image': inputs.image.tolist(),
        }
        response = requests.post(
            str(self.settings.host_Text_detector), json=payload,
        )

        return TextDectorOutput(
            class_list=response.json()['info']['class_list'],
            bboxes_list=response.json()['info']['bboxes'],
            conf_list=response.json()['info']['conf_list'],
        )
