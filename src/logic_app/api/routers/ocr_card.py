from __future__ import annotations

import cv2
import numpy as np
from api.helper.exception_handler import ExceptionHandler
from api.helper.exception_handler import ResponseMessage
from app.ocr import OCRInput
from app.ocr import OCRService
from common.logs import get_logger
from common.utils import get_settings
from fastapi import APIRouter
from fastapi import File
from fastapi import status
from fastapi import UploadFile
from fastapi.encoders import jsonable_encoder


ocr = APIRouter(prefix='/v1')
logger = get_logger(__name__)

settings = get_settings()


# Define API input


@ocr.post(
    '/ocr',
    # response_model=APIOutput,
    responses={
        status.HTTP_200_OK: {
            'content': {
                'application/json': {
                    'example': {
                        'message': ResponseMessage.SUCCESS,
                        'info': {
                            'status': True,
                        },
                    },
                },
            },
        },
        status.HTTP_400_BAD_REQUEST: {
            'description': 'Bad Request',
            'content': {
                'application/json': {
                    'example': {
                        'message': ResponseMessage.BAD_REQUEST,
                    },
                },
            },
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            'description': 'Internal Server Error',
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
async def ocr_card(file: UploadFile = File(...)):
    exception_handler = ExceptionHandler(
        logger=logger.bind(), service_name=__name__,
    )

    # Read image from UploadFile
    try:
        contents = await file.read()

        # Convert the raw image data into a NumPy array
        nparr = np.frombuffer(contents, np.uint8)

        # Decode the NumPy array into an OpenCV (BGR) image
        img_array = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    except Exception as e:
        return exception_handler.handle_exception(
            e=f'Error while reading file: {e}',
            extra={'file_name': file.filename},
        )
    # Define application
    try:
        logger.info('Load mode card checkin !!!')
        ocr_model = OCRService(settings=settings)
    except Exception as e:
        return exception_handler.handle_exception(
            f'Failed to initialize card checkin model: {e}',
            extra={'file_name': file.filename},
        )
    # infer
    try:
        text_ocr_result = ocr_model.process(
            inputs=OCRInput(image=img_array),
        )
        return exception_handler.handle_success(jsonable_encoder(text_ocr_result))
    # except FaceValidateException as e:
    #     return exception_handler.handle_bad_request(
    #         message=f'Face validation failed: {e}',
    #         extra={'face_image': file.filename},
    #     )
    except Exception as e:
        return exception_handler.handle_exception(
            e=f'Error while reading file: {e}',
            extra={'file_name': file.filename},
        )
