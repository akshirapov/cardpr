
import os
import json
import time

from pathlib import Path
from app import app


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
    """
    Return list of hooks.
    """
    hooks = []
    for filename in get_hooks_list():
        data = read_hook(filename)
        hooks.append(data)
    return {'hooks': hooks}


def get_hook_filename():
    """
    Returns the name for the hook.

    'name = hook_<timestamp>.json'
    """
    folder = get_hooks_folder()
    name = os.path.join(
        folder,
        f'hook_{time.time()}.json'
    )
    return name


def get_hooks_folder():
    """
    Returns folder of stored hook files.
    """
    folder = app.config['BASE_DIR'] + '/hooks'
    Path(folder).mkdir(parents=True, exist_ok=True)
    return folder


def get_hooks_list():
    """
    Return list of hook files.
    """
    filenames = []
    folder = get_hooks_folder()
    for root, dirs, files in os.walk(folder):
        for file in files:
            filenames.append(os.path.join(root, file))
    return filenames


def read_hook(filename):
    """
    Reads json data from a file.
    """
    with open(filename, encoding='utf-8') as f:
        return json.loads(f.read())


def save_hook(data: dict):
    """
    Saves json data to a file.
    """
    filename = get_hook_filename()
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
