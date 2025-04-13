from __future__ import annotations

import asyncio
import unittest

import cv2
from common import get_settings
from infrastructure.text_ocr import TextOCRModel
from infrastructure.text_ocr import TextOCRModelInput


class TestTextOCROnly(unittest.TestCase):

    def setUp(self) -> None:
        self.settings = get_settings()
        self.text_ocr = TextOCRModel(settings=self.settings)

    def test_text_ocr(self):
        # Đường dẫn ảnh cần test
        image_path = '/home/anodi108/Desktop/project/Do_An_Tot_Nghiep/DATN_LuThiSen/src/model_deployed/text_detector_preproces.png'
        img = cv2.imread(image_path)
        self.assertIsNotNone(img, 'Ảnh không được load thành công!')

        # Danh sách class và bbox giả định (phải đúng với ảnh)
        class_list = ['name', 'dob']
        bboxes_list = [
            [400, 200, 900, 300],  # x_min, y_min, x_max, y_max
            [400, 310, 900, 400],
        ]

        # Tạo input
        text_input = TextOCRModelInput(
            img=img,
            class_list=class_list,
            bboxes_list=bboxes_list,
        )

        # Gọi hàm xử lý
        text_output = asyncio.run(self.text_ocr.process(text_input))

        # In kết quả
        for result in text_output.results:
            print('Class:', result['class'])
            print('Bounding box:', result['bounding_box'])
            print('Text:', result['text'])
            print('-' * 50)

        # Vẽ kết quả lên ảnh
        img_output = img.copy()
        for result in text_output.results:
            x1, y1, x2, y2 = map(int, result['bounding_box'])
            cls = result['class']
            text = result['text']

            cv2.rectangle(img_output, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(
                img_output,
                f'{cls}: {text}',
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 0, 0),
                2,
            )

        # Lưu ảnh kết quả
        cv2.imwrite('text_ocr_output.png', img_output)


if __name__ == '__main__':
    unittest.main()
