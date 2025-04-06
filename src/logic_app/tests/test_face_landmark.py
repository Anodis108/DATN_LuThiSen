# from __future__ import annotations
# import sys
# import unittest
# from pathlib import Path
# import numpy as np
# from appplication.infrastructure.text_ocr.text_ocr import FaceLandMark
# from appplication.infrastructure.text_ocr.text_ocr import FaceLandMarkInput
# from common.utils import get_settings
# sys.path.append(str(Path(__file__).parent.parent))  # type: ignore
# class TestFaceLandMark(unittest.TestCase):
#     def setUp(self) -> None:
#         self.settings = get_settings()
#         self.face_landmark = FaceLandMark(settings=self.settings)
#     def test_api_landmark(self):
#         loaded_embedding = np.load(
#             '/home/hungtech/hdev/AI_Face-login-final/src/model_deployed/tests/embedding.npy',
#         )
#         print(
#             'Image shape:', loaded_embedding.shape,
#             'dtype:', loaded_embedding.dtype,
#         )
#         bbox = [
#             5.2817487e+02, 3.8963406e+02,
#             9.2570911e+02, 8.6887885e+02, 8.3381450e-01,
#         ]
#         result = self.face_landmark.process(
#             inputs=FaceLandMarkInput(
#                 image=loaded_embedding,
#                 bbox=bbox,
#             ),
#         )
#         print(result)
from __future__ import annotations
