"""
Web app main
"""
import logging

import requests
from flask import Flask, request, jsonify, make_response, Response
from requests.exceptions import ConnectionError

from config.envs import EXAMPLE_ENV_VAR

logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route('/example/route', methods=['POST'])
def example_post() -> Response:
    """
    POST example.
    """
    # We retrieve JSON data from the request
    message_dictionary = request.get_json()

    logger.debug(message_dictionary)

    headers = {'Content-Type': 'application/json'}

    try:
        app_response = jsonify({ 'example': EXAMPLE_ENV_VAR, 'data': message_dictionary })
        app_response.status_code = 500
        return app_response
    except Exception as e:
        logger.error(f'Error in example1')
        logger.exception(e)
        app_response = jsonify({"status": 500, "message": f"Error in example_post"})
        app_response.status_code = 500
        return app_response


@app.route('/example/<data1>/test/<int:data2>', methods=['GET'])
def example_get(data1: str, data2: int) -> Response:
    """
    GET example.
    """
    try:
        app_response = jsonify({"data1": data1, "data2": data2, "query_params": request.args })
        app_response.status_code = 500
        return app_response
    except Exception as e:
        logger.error(f'Error in ')
        logger.exception(e)
        app_response = jsonify(
            {"status": 500, "message": f"Error in example_get"})
        app_response.status_code = 500
        return app_response
