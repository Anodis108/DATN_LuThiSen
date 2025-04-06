# from __future__ import annotations
# import unittest
# import numpy as np
# from common.utils import get_settings
# # from infra.embedding import FaceEmbedding
# # from infra.embedding import FaceEmbeddingInput
# class TestFaceEmbedding(unittest.TestCase):
#     def setUp(self) -> None:
#         self.settings = get_settings()
#         self.face_mbedding = FaceEmbedding(settings=self.settings)
#     def test_api_embedding(self):
#         loaded_embedding = np.load(
#             '/home/nguyen.luong.hung@sun-asterisk.com/PoC/AI_Face-login/src/model_deployed/tests/embedding.npy',
#         )
#         print(
#             'Image shape:', loaded_embedding.shape,
#             'dtype:', loaded_embedding.dtype,
#         )
#         kpoint = np.array([
#             [191.55109, 180.67368],
#             [234.27043, 179.21089],
#             [214.12573, 203.67413],
#             [198.07564, 226.53897],
#             [230.68082, 225.25124],
#         ])
#         inputs = FaceEmbeddingInput(image=loaded_embedding, kpps=kpoint)
#         result = self.face_mbedding.process(inputs=inputs)
#         print(result.embedding)
from __future__ import annotations
