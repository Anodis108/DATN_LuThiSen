# from __future__ import annotations
# import unittest
# import numpy as np
# from common.utils import get_settings
# from fastapi.encoders import jsonable_encoder
# # from infrastructure.card_detector import FaceDetector
# # from infrastructure.card_detector import FaceDetectorInput
# class TestFaceEmbedding(unittest.TestCase):
#     def setUp(self) -> None:
#         self.settings = get_settings()
#         self.face_detector = FaceDetector(settings=self.settings)
#     def test_api_embedding(self):
#         loaded_embedding = np.load(
#             '/home/nguyen.luong.hung@sun-asterisk.com/PoC/AI_Face-login/src/model_deployed/tests/embedding.npy',
#         )
#         print(
#             'Image shape:', loaded_embedding.shape,
#             'dtype:', loaded_embedding.dtype,
#         )
#         inputs = FaceDetectorInput(image=loaded_embedding)
#         result = self.face_detector.process(inputs=inputs)
#         print(jsonable_encoder(result))
from __future__ import annotations
