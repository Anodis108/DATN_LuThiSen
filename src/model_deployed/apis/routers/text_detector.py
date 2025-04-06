from __future__ import annotations

import numpy as np
from apis.helper.exception_handler import ExceptionHandler
from apis.helper.exception_handler import ResponseMessage
from apis.models.text_detector import APIInput
from apis.models.text_detector import APIOutput
from common.logs import get_logger
from common.utils import get_settings
from fastapi import APIRouter
from fastapi import Body
from fastapi import status
from fastapi.encoders import jsonable_encoder
from infrastructure.text_detector import TextDetectorModel
from infrastructure.text_detector import TextDetectorModelInput

# import cv2

text_detector = APIRouter(prefix='/v1')
logger = get_logger(__name__)
settings = get_settings()


try:
    logger.info('Load mode Text detector !!!')
    text_detector_model = TextDetectorModel(settings=settings)
except Exception as e:
    logger.error(f'Failed to initialize Text embedding model: {e}')
    raise e  # stop and display full error message


@text_detector.post(
    '/text_detector',
    response_model=APIOutput,
    responses={
        status.HTTP_200_OK: {
            'content': {
                'application/json': {
                    'example': {
                        'message': ResponseMessage.SUCCESS,
                        'info': {
                            'bboxes': [[1, 1, 1, 1]],
                        },
                    },
                },
            },
        },
        status.HTTP_400_BAD_REQUEST: {
            'description': 'Bad Request - message is required',
            'content': {
                'application/json': {
                    'example': {
                        'message': ResponseMessage.BAD_REQUEST,
                    },
                },
            },
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            'description': 'Internal Server Error - Error during init conversation',
            'content': {
                'application/json': {
                    'example': {
                        'message': ResponseMessage.INTERNAL_SERVER_ERROR,
                    },
                },
            },
        },
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            'description': 'Unprocessable Entity - Format is not supported',
            'content': {
                'application/json': {
                    'example': {
                        'message': ResponseMessage.UNPROCESSABLE_ENTITY,
                    },
                },
            },
        },
        status.HTTP_404_NOT_FOUND: {
            'description': 'Destination Not Found',
            'content': {
                'application/json': {
                    'example': {
                        'message': ResponseMessage.NOT_FOUND,
                    },
                },
            },
        },
    },
)
async def text_detect(inputs: APIInput = Body(...)):
    """
    Detects texts in the provided image.

    Args:
        inputs (APIInput): Input containing image data.

    Returns:
        JSON response containing detected texts and bounding boxes.
    """

    exception_handler = ExceptionHandler(
        logger=logger.bind(), service_name=__name__,
    )

    # Kiểm tra đầu vào hợp lệ
    if inputs is None or not inputs.img:
        return exception_handler.handle_bad_request(
            'Invalid image data',
            jsonable_encoder(inputs),
        )

    try:
        logger.info(f'Processing text detection for input: {inputs}')

        # Chuyển đổi ảnh từ list về numpy array
        img_array = np.array(inputs.img, dtype=np.uint8)

        # Gọi model phát hiện văn bản
        response = await text_detector_model.process(
            inputs=TextDetectorModelInput(
                img=img_array,
            ),
        )

        # Kiểm tra kết quả phát hiện văn bản
        if not response.bboxes_list:
            return exception_handler.handle_unprocessable_entity(
                'No text detected in the image',
                jsonable_encoder(inputs),
            )

        # Trả về kết quả
        api_output = APIOutput(
            bboxes=response.bboxes_list,  # type: ignore
            classes=response.class_list,  # type: ignore
            confs=response.conf_list,  # type: ignore
        )

        logger.info('Text detection completed successfully.')
        return exception_handler.handle_success(jsonable_encoder(api_output))

    except Exception as e:
        logger.exception(
            f'Exception occurred while processing text detection: {e}',
        )
        return exception_handler.handle_exception(
            'Failed to process text detection',
            jsonable_encoder(inputs),
        )
