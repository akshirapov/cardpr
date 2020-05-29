
from app import app
from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response


@app.errorhandler(400)
def bad_request(error):
    return error_response(error.code)


@app.errorhandler(403)
def forbidden_error(error):
    return error_response(error.code)


@app.errorhandler(404)
def not_found_error(error):
    return error_response(error.code)


@app.errorhandler(405)
def method_not_allowed_error(error):
    return error_response(error.code)


@app.errorhandler(500)
def unexpected_error(error):
    return error_response(error.code)
