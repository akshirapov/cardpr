
from app import app
from flask import request, jsonify
from app import hooks
from .errors import error_response


supported_methods = [
    'createCustomer',
    'updateCustomer',
    # 'readBalance',
    # 'addBalance',
]


@app.route('/hook', methods=['POST'])
def hook():
    data = request.get_json() or {}
    if 'method' not in data:
        return error_response(400, 'Must Include Method.')

    method = data['method']
    if method not in supported_methods:
        return error_response(400, f'Unsupported Method [{method}]')

    result = hooks.process_hook(data)
    if result:
        response = jsonify(result)
        response.status_code = 201
        return response
    return error_response(400)


@app.route('/hooks', methods=['GET'])
def get_hooks():
    result = hooks.get_hooks()
    if result:
        response = jsonify(result)
        response.status_code = 200
        return response
    return error_response(400)
