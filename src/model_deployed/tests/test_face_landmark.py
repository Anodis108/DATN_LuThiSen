# from __future__ import annotations
# import unittest
# import numpy as np
# from infrastructure.face_landmark import FaceLandMark
# from infrastructure.face_landmark import FaceLandMarkInput
# from common import get_settings
# class TestFaceEmbedding(unittest.TestCase):
#     def setUp(self) -> None:
#         self.settings = get_settings()
#         self.face_landmark_model = FaceLandMark(settings=self.settings)
#     def test_embedding(self):
#         loaded_embedding = np.load(
#             '/home/nguyen.luong.hung@sun-asterisk.com/PoC/AI_Face-login/src/model_deployed/tests/embedding_landmark.npy',
#         )
#         bbox = [
#             5.2817487e+02, 3.8963406e+02,
#             9.2570911e+02, 8.6887885e+02, 8.3381450e-01,
#         ]
#         result = self.face_landmark_model.process(
#             inputs=FaceLandMarkInput(
#                 img=loaded_embedding,
#                 bbox=bbox,
#             ),
#         )
#         print(result)
from __future__ import annotations
