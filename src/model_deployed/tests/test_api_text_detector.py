from __future__ import annotations

import base64
import unittest
from io import BytesIO

import numpy as np
import requests  # type: ignore
from PIL import Image
# from apis.models.text_detector import APIInput
# from apis.models.text_detector import APIOutput


class TestTextDetectorAPI(unittest.TestCase):

    def setUp(self) -> None:
        """Cài đặt ban đầu"""
        self.image_path = '/home/anodi108/Desktop/project/Do_An_Tot_Nghiep/DATN_LuThiSen/src/model_deployed/demo_card.npy'
        self.api_url = 'http://localhost:5000/v1/text_detector'  # URL của API

    def test_text_detector(self):
        """Test API Text Detector"""
        loaded_embedding = np.load(self.image_path)
        print('Loaded shape:', loaded_embedding.shape)  # Phải là (H, W, 3)
        print(
            'Is RGB image:', loaded_embedding.ndim ==
            3 and loaded_embedding.shape[2] == 3,
        )

        # Chuyển thành list 3D
        image_data = loaded_embedding.astype(np.uint8)

        # Kiểm tra bbox
        bbox = np.array([341.92, 896.35, 1506.26, 1659.61], dtype=float)
        print(
            'Image shape:', loaded_embedding.shape,
            'dtype:', loaded_embedding.dtype,
        )

        # Tạo một bounding box mẫu (có thể cần điều chỉnh theo yêu cầu của bạn)
        bbox = np.array([
            341.9267578125, 896.35986328125,
            1506.2652587890625, 1659.611328125,
        ])

        # Tạo payload
        payload = {
            'img_origin': image_data.tolist(),  # Chuyển ảnh thành base64 string
            'bbox': bbox.tolist(),
        }

        # Gửi yêu cầu POST đến API
        response = requests.post(self.api_url, json=payload)
        print('Raw response:', response.text)

        # In status code và response JSON để kiểm tra
        print(f'Status Code: {response.status_code}')
        print(f'Response JSON: {response.json()}')

        # Kiểm tra mã phản hồi và xác nhận kết quả
        # Kiểm tra code trả về là 200 OK
        self.assertEqual(response.status_code, 200)
        response_json = response.json()

        # Kiểm tra thông điệp trả về
        self.assertIn('message', response_json)
        self.assertEqual(response_json['message'], 'Process successfully !!!')

        # Kiểm tra bboxes
        self.assertIn('info', response_json)
        self.assertIn('bboxes', response_json['info'])
        self.assertIsInstance(response_json['info']['bboxes'], list)
        self.assertGreater(len(response_json['info']['bboxes']), 0)

    def base64_to_image_list(self, base64_str: str) -> list:
        """Chuyển đổi base64 string thành danh sách 3D để phù hợp với APIInput"""
        image_data = base64.b64decode(base64_str)
        image = Image.open(BytesIO(image_data))

        # Chuyển hình ảnh thành numpy array và chuẩn hóa thành list 3D
        image_np = np.array(image)
        image_list = image_np.tolist()

        return image_list


if __name__ == '__main__':
    unittest.main()
