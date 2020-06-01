from app import app, hooks, errors
from flask import request, jsonify


supported_methods = [
    'createCustomer',
    'updateCustomer',
    'readBalance',
    'addBalance',
]


@app.route('/cardpr', methods=['POST'])
def hook():
    data = request.get_json() or {}
    if 'method' not in data:
        return errors.error_response(400, 'Must Include Method.')

    method = data['method']
    if method not in supported_methods:
        return errors.error_response(400, f'Unsupported Method [{method}]')

    result = hooks.process_hook(data)
    if result:
        response = jsonify(result)
        response.status_code = 201
        return response
    return errors.error_response(500)


@app.route('/cardpr/hooks', methods=['GET'])
def get_hooks():
    result = hooks.get_hooks()
    response = jsonify(result)
    response.status_code = 200
    return response


@app.route('/cardpr/hooks/<int:hook_id>', methods=['PUT'])
def complete_hook(hook_id):
    result = hooks.complete_hook(hook_id)
    response = jsonify(result)
    response.status_code = 200
    return response
