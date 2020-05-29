
__all__ = [
    'process_hook',
    'get_hooks',
]

import os
import json
import time

from pathlib import Path
from app import app


def get_filename():
    """
    Returns the name for the hook.

    'name = hook_timestamp.json'
    """
    folder = app.config['BASE_DIR'] + '/hooks'
    Path(folder).mkdir(parents=True, exist_ok=True)

    name = os.path.join(
        folder,
        f'hook_{time.time()}.json'
    )
    return name


def save_hook(data: dict):
    """
    Saves json data to a file.
    """
    filename = get_filename()
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def create_customer(data: dict):
    """
    Create a customer
    """
    save_hook(data)
    result = {
        'customerId': ''
    }
    return result


def update_customer(data: dict):
    save_hook(data)
    result = {
        'customerId': ''
    }
    return result


def read_balance(data: dict):
    result = {
        'success': False,
        'bonus': 0,
        'balance': 0,
        'discount': 0
    }
    return result


def add_balance(data: dict):
    result = {
        'success': False,
    }
    return result


def process_hook(data: dict):

    result = dict()

    method = data['method']
    if method == 'createCustomer':
        result = create_customer(data)
    elif method == 'updateCustomer':
        result = update_customer(data)
    elif method == 'readBalance':
        result = read_balance(data)
    elif method == 'addBalance':
        result = add_balance(data)

    return result


def get_hooks():
    data = [
        {'hook': '1590750875.7095132_createCustomer'},
        {'hook': '1590751219.9904015_createCustomer'},
        {'hook': '1590751220.783476_updateCustomer'}
    ]
    return {'hooks': data}
