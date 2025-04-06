from __future__ import annotations

import unittest

import numpy as np
from infrastructure.face_embedding import FaceEmbeddingModel
from infrastructure.face_embedding import FaceEmbeddingModelInput
from shared import get_settings


class TestFaceEmbedding(unittest.TestCase):
    def setUp(self) -> None:
        self.settings = get_settings()
        self.face_embedding_model = FaceEmbeddingModel(settings=self.settings)

    def test_embedding(self):
        loaded_embedding = np.load(
            '/home/anodi108/Desktop/project/AI_Face-login_After_clean/AI_Face-login/src/model_deployed/tests/output.npy',
        )

        kpoint = np.array([
            [191.55109, 180.67368],
            [234.27043, 179.21089],
            [214.12573, 203.67413],
            [198.07564, 226.53897],
            [230.68082, 225.25124],
        ])
        result = self.face_embedding_model.process(
            inputs=FaceEmbeddingModelInput(
                image=loaded_embedding,
                kps=kpoint,
            ),
        )
        print(result)


if __name__ == '__main__':
    unittest.main()
