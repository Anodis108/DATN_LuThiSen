# from __future__ import annotations
# import unittest
# import cv2
# from infrastructure.card_detector import FaceDetectorModel
# from infrastructure.card_detector import FaceDetectorModelInput
# from shared import get_settings
# class TestFaceDetector(unittest.TestCase):
#     def setUp(self) -> None:
#         self.settings = get_settings()
#         self.face_detector_model = FaceDetectorModel(settings=self.settings)
#     def test_detect(self):
#         image_path = '/home/nguyen.luong.hung@sun-asterisk.com/PoC/AI_Face-login/src/model_deployed/tests/HoangPhuonganh the.jpg'
#         img = cv2.imread(image_path)
#         print(img)
#         # Chuyển sang RGB
#         # Kiểm tra giá trị pixel đầu tiên (tại vị trí 0,0)
#         b, g, r = img[0, 0]
#         # Nếu giá trị B khác giá trị R, nhiều khả năng ảnh đang ở định dạng BGR
#         if b != r:
#             print('Ảnh đang ở định dạng BGR')
#         else:
#             print('Ảnh có thể là RGB hoặc ảnh đơn sắc')
#         inputs = FaceDetectorModelInput(
#             img=img,
#         )
#         import asyncio
#         outputs = asyncio.run(self.face_detector_model.process(inputs))
#         print(outputs.bboxes)
#         print('-------')
#         print(outputs.kpss)
#         bbox = outputs.bboxes[0][:4]
#         confidence = outputs.bboxes[0][-1]
#         keypoints = outputs.kpss[0]  # type: ignore
#         # Vẽ bounding box
#         x1, y1, x2, y2 = map(int, bbox)
#         cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#         cv2.putText(
#             img, f'Conf: {confidence:.2f}', (x1, y1 - 10),
#             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2,
#         )
#         # Vẽ keypoints
#         for (x, y) in keypoints:
#             cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
#         cv2.imwrite('output.png', img)
from __future__ import annotations
