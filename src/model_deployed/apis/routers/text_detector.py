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
    if inputs is None or not inputs.image:
        return exception_handler.handle_bad_request(
            'Invalid image data',
            jsonable_encoder(inputs),
        )

    try:
        logger.info(f'Processing text detection for input: {inputs}')

        # Chuyển ảnh và bbox sang numpy
        img_array = np.array(inputs.image, dtype=np.uint8)
        bbox_np = np.array(inputs.bbox, dtype=np.int32)

        if img_array.ndim != 3:
            raise ValueError('Input image must be a 3D RGB array')

        if bbox_np.shape != (4,):
            raise ValueError('Bounding box must be a list of 4 float values')

        # Gọi model xử lý
        response = await text_detector_model.process(
            inputs=TextDetectorModelInput(
                img_origin=img_array,
                bbox=bbox_np,
            ),
        )

        if not response.bboxes_list:
            return exception_handler.handle_unprocessable_entity(
                'No text detected in the image',
                jsonable_encoder(inputs),
            )

        # Tạo response model
        api_output = APIOutput(
            bboxes=response.bboxes_list,
            classes=response.class_list,
            confs=response.conf_list,
        )

        logger.info('Text detection completed successfully.')
        return exception_handler.handle_success(jsonable_encoder(api_output))

    except ValueError as ve:
        return exception_handler.handle_bad_request(str(ve), jsonable_encoder(inputs))

    except TypeError as te:
        return exception_handler.handle_bad_request(str(te), jsonable_encoder(inputs))

    except FileNotFoundError as fnf:
        return exception_handler.handle_not_found_error(str(fnf), jsonable_encoder(inputs))

    except RuntimeError as re:
        return exception_handler.handle_exception(str(re), jsonable_encoder(inputs))

    except Exception as e:
        logger.exception(
            f'Exception occurred while processing text detection: {e}',
        )
        return exception_handler.handle_exception(
            'Failed to process text detection',
            jsonable_encoder(inputs),
        )
