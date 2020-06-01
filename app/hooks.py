import json

from app import app, db
from app.models import Hook


def get_hooks():
    """
    Return list of hooks.
    """
    result = []

    hooks = Hook.query.filter_by(complete=False).order_by(Hook.timestamp.asc())
    for h in hooks:
        data = json.loads(h.body)
        data['id'] = h.id
        rename_cts(data)
        result.append(data)

    return {'hooks': result}


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


def save_hook(data: dict):
    """
    Saves data to a database.
    """
    hook = Hook()
    hook.body = json.dumps(data, ensure_ascii=False, indent=4)
    db.session.add(hook)
    db.session.commit()


def complete_hook():
    """
    Mark the hook as complete.
    """


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
    save_hook(data)
    result = {
        'success': False,
        'bonus': 0,
        'balance': 0,
        'discount': 0
    }
    return result


def add_balance(data: dict):
    save_hook(data)
    result = {
        'success': False,
    }
    return result


def rename_cts(data: dict):
    if 'customer' in data and 'cardTracks' in data['customer']:
        cts_org = data['customer']['cardTracks']
        cts_new = dict()
        for ct in cts_org.keys():
            cts_new[f'ct_{ct}'] = cts_org[ct]
        data['customer']['cardTracks'] = cts_new
