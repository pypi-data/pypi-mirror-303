import json
import logging
from functools import wraps
from typing import Type, Tuple, Any, Union

from flask import jsonify, Request, Response
from flask import request as incoming_request
from pydantic import BaseModel, ValidationError
from requests import HTTPError, RequestException
from werkzeug.exceptions import BadRequest

from easyflowutils.logger_utils import configure_cloud_logger

VALIDATION_ERROR_STATUS_CODE = 422


def log_and_return_response(response: Union[Tuple[Any, int], Response]) -> Union[Tuple[Any, int], Response]:
    try:
        if isinstance(response, tuple):
            content, status_code = response
        elif isinstance(response, Response):
            content = response
            status_code = response.status_code
        else:
            logging.warning(f"Unexpected response type: {type(response)}")
            return response

        log_message = f"Returning response: Status: {status_code}"

        if isinstance(content, Response):
            response_data = content.get_data(as_text=True)
            log_message += f", Body: {response_data}"
        elif isinstance(content, dict):
            response_data = json.dumps(content)
            log_message += f", Body: {response_data}"
        else:
            response_data = str(content)
            log_message += f", Body: {response_data}"

        logging.info(log_message)
    except Exception as e:
        logging.warning(f"Error in log_and_return_response: {str(e)}")

    return response


def validate_request(request_model: Type[BaseModel]):
    configure_cloud_logger()

    def decorator(func):
        @wraps(func)
        def wrapper(request: Request, *args, **kwargs):
            try:
                request_json = request.get_json()
                logging.info(f"Received request: {request_json or {} }")
                if not request_json:
                    return log_and_return_response(
                        (jsonify({"error": "Request body is empty"}), VALIDATION_ERROR_STATUS_CODE))

                validated_data = request_model(**request_json)

                return log_and_return_response(func(validated_data, *args, **kwargs))

            except ValidationError as e:
                error_messages = []
                for error in e.errors():
                    error_messages.append(f"{error['loc'][0]}: {error['msg']}")

                error_response = {
                    "error": "Validation failed",
                    "details": error_messages
                }
                logging.warning(f"Validation error: {error_response}")
                return jsonify(error_response), VALIDATION_ERROR_STATUS_CODE

            except HTTPError as e:
                status_code = e.response.status_code if e.response.status_code else 500
                error_message = str(e)
                try:
                    error_json = e.response.json()
                    logging.error(f"HTTP error: {error_message}, status code: {status_code}, error JSON: {error_json}")
                    return jsonify(
                        {"error": f"An HTTP error occurred: {error_message}", "details": error_json}), status_code
                except ValueError:
                    logging.error(f"HTTP error: {error_message}, status code: {status_code}")
                    return jsonify({"error": f"An HTTP error occurred: {error_message}"}), status_code

            except RequestException as e:
                logging.error(f"Request error: {str(e)}")
                return jsonify({"error": f"A network error occurred: {str(e)}"}), 503

            except Exception as e:
                logging.error(f"Unexpected error: {str(e)}")
                return jsonify({"error": f"An unexpected error occurred, {str(e)}"}), 500

        return wrapper

    return decorator


def validate_cloud_run_request(model):
    configure_cloud_logger()

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                try:
                    json_data = incoming_request.get_json(force=True)
                except BadRequest:
                    json_data = {}

                logging.info(f"Received request: {json_data or {} }")

                if json_data is None:
                    return log_and_return_response(
                        (jsonify({"error": "Request body is empty"}), VALIDATION_ERROR_STATUS_CODE))

                validated_data = model(**json_data)
                return log_and_return_response(func(validated_data, *args, **kwargs))

            except ValidationError as e:
                error_messages = []
                for error in e.errors():
                    error_messages.append(f"{error['loc'][0]}: {error['msg']}")

                error_response = {
                    "error": "Validation failed",
                    "details": error_messages
                }

                logging.warning(f"Validation error: {error_response}")
                return jsonify(error_response), VALIDATION_ERROR_STATUS_CODE

            except HTTPError as e:
                status_code = e.response.status_code if e.response.status_code else 500
                error_message = str(e)

                try:
                    error_json = e.response.json()
                    logging.error(f"HTTP error: {error_message}, status code: {status_code}, error JSON: {error_json}")
                    return jsonify(
                        {"error": f"An HTTP error occurred: {error_message}", "details": error_json}), status_code

                except ValueError:
                    logging.error(f"HTTP error: {error_message}, status code: {status_code}")
                    return jsonify({"error": f"An HTTP error occurred: {error_message}"}), status_code

            except RequestException as e:
                logging.error(f"Request error: {str(e)}")
                return jsonify({"error": f"A network error occurred: {str(e)}"}), 503

            except Exception as e:
                logging.error(f"Unexpected error: {str(e)}")
                return jsonify({"error": f"An unexpected error occurred, {str(e)}"}), 500

        return wrapper

    return decorator
