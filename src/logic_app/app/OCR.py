from __future__ import annotations

# import numpy as np
# from common.bases import BaseModel
# from common.bases import BaseService
# from common.logs import get_logger
# from common.settings import Settings
# from infrastructure.card_detector import CardDetector
# from infrastructure.card_detector import CardDetectorInput
# from infrastructure.text_detector import TextDetector
# from infrastructure.text_detector import TextDetectorInput
# from infrastructure.text_ocr import TextOCR
# from infrastructure.text_ocr import TextOCRInput
# # from domain.face_validator import FaceValidatorInput
# # from domain.face_validator import FaceValidatorService
# # from shared.exceptions import FaceValidateException
# logger = get_logger(__name__)


# class OCRInput(BaseModel):
#     image: np.ndarray


# class OCROutput(BaseModel):
#     status: bool


# class OCRService(BaseService):
#     settings: Settings

#     @property
#     def _get_card_detector(self) -> CardDetector:
#         return CardDetector(settings=self.settings)

#     @property
#     def _get_text_detector(self) -> TextDetector:
#         return TextDetector(settings=self.settings)

#     @property
#     def _get_text_ocr(self) -> TextOCR:
#         return TextOCR(settings=self.settings)

#     def process(self, inputs: OCRInput) -> OCROutput:
#         # detect card
#         try:
#             card_det_output = self._get_card_detector.process(
#                 inputs=CardDetectorInput(
#                     image=inputs.image,
#                 ),
#             )
#         except Exception as e:
#             logger.error(f'Failed to process card detection: {e}')
#             raise e  # stop and display full error message
#         # card alige (Sẽ đc thực hiện ở API card detect đc gọi)
#         card_align = None  # Img sau khi ddc crop
#         # detext text
#         try:
#             text_det_out = self._get_text_detector.process(
#                 inputs=TextDetectorInput(
#                     image=card_align,
#                 ),
#             )
#         except Exception as e:
#             logger.error(f'Failed to process card detection: {e}')
#             raise e  # stop and display full error message
#         # Card_black_white
#         card_black_white = None
#         # text ocr
#         try:
#             text_ocr_out = self._get_text_ocr.process(
#                 inputs=TextOCRInput(
#                     img=card_black_white,
#                     bboxes_list=text_det_out.bboxes_list,
#                     class_list=text_det_out.class_list,
#                 ),
#             )
#             # if not text_ocr_out.results :
#             #     raise FaceValidateException('Face not satisfied !!!')
#         except Exception as e:
#             logger.error(f'Failed to text ocr: {e}')
#             return OCROutput(status=False)
#         return OCROutput(status=True)
