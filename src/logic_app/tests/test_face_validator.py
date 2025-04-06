# from __future__ import annotations
# import sys
# import unittest
# from pathlib import Path
# import numpy as np
# from common.logs import get_logger
# from common.utils import get_settings
# from service.face_validator.service import FaceValidatorInput
# from service.face_validator.service import FaceValidatorService
# sys.path.append(str(Path(__file__).parent.parent))
# logger = get_logger(__name__)
# class TestFaceValidatorService(unittest.TestCase):
#     def setUp(self) -> None:
#         self.settings = get_settings()
#         self.service = FaceValidatorService(settings=self.settings)
#     def test_no_bboxes_provided(self):
#         inputs = FaceValidatorInput(
#             image=np.ones((100, 100, 3), dtype=np.uint8) * 255,
#             bboxes=np.array([]),
#             kpss=None,
#         )
#         result = self.service.process(inputs=inputs)
#         self.assertIsNone(result.bboxes)
#         self.assertIsNone(result.kpss)
#     def test_valid_bboxes_and_kpss(self):
#         image = np.ones((100, 100, 3), dtype=np.uint8) * 255
#         bboxes = np.array([
#             [10, 10, 50, 50, 0.9],
#             [20, 20, 60, 60, 0.8],
#             [30, 30, 70, 70, 0.7],
#         ])
#         kpss = np.array([
#             [[15, 15], [35, 15], [25, 35], [15, 35], [35, 35]],
#             [[25, 25], [45, 25], [35, 45], [25, 45], [45, 45]],
#             [[35, 35], [55, 35], [45, 55], [35, 55], [55, 55]],
#         ])
#         inputs = FaceValidatorInput(
#             image=image,
#             bboxes=bboxes,
#             kpss=kpss,
#         )
#         result = self.service.process(inputs=inputs)
#         if result.bboxes is None:
#             self.assertIsNone(result.bboxes)
#         else:
#             np.testing.assert_array_equal(
#                 result.bboxes,
#                 np.array([10, 10, 50, 50, 0.9]),
#             )  # type: ignore
#         if result.kpss is None:
#             self.assertIsNone(result.kpss)
#         else:
#             np.testing.assert_array_equal(
#                 result.kpss, np.array(
#                     [[15, 15], [35, 15], [25, 35], [15, 35], [35, 35]],
#                 ),
#             )  # type: ignore
#     def test_invalid_bboxes(self):
#         image = np.ones((100, 100, 3), dtype=np.uint8) * 255
#         bboxes = np.array([
#             [10, 10, 50, 50, 0.4],  # Below threshold
#             [20, 20, 10, 10, 0.9],  # Invalid bbox
#         ])  # type: ignore
#         kpss = None
#         inputs = FaceValidatorInput(
#             image=image,
#             bboxes=bboxes,
#             kpss=kpss,
#         )
#         result = self.service.process(inputs=inputs)
#         self.assertIsNone(result.bboxes)
#         self.assertIsNone(result.kpss)
#     def test_valid_face_angle(self):
#         image = np.load(
#             '/home/chien/code/AI_Face-login/src/model_deployed/tests/MESSI.npy',
#         )
#         bboxes = np.array([
#             [
#                 92.3033447265625,
#                 90.44351959228516,
#                 223.68727111816406,
#                 290.9163818359375,
#                 0.8588523268699646,
#             ],
#         ])
#         kpss = np.array([[
#             [
#                 129.91799926757812,
#                 166.3173370361328,
#             ],
#             [
#                 188.44476318359375,
#                 168.41397094726562,
#             ],
#             [
#                 159.58209228515625,
#                 203.80868530273438,
#             ],
#             [
#                 129.83541870117188,
#                 232.83119201660156,
#             ],
#             [
#                 182.66448974609375,
#                 234.84361267089844,
#             ],
#         ]])
#         inputs = FaceValidatorInput(
#             image=image,
#             bboxes=bboxes,
#             kpss=kpss,
#         )
#         result = self.service.process(inputs=inputs)
#         self.assertIsNotNone(result.bboxes)
#         self.assertIsNotNone(result.kpss)
# if __name__ == '__main__':
#     unittest.main()
from __future__ import annotations
