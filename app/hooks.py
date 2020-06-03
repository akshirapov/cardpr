import json

from app import db
from app import crm
from app.models import Hook


def get_hooks():
    """
    Returns the list of uncompleted hooks.
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
    """
    Processes the received hook.
    """

    result = dict()
    save_hook(data)

    method = data['method']
    if method == 'createCustomer':
        result = crm.create_customer(data)
    elif method == 'updateCustomer':
        result = crm.update_customer(data)
    elif method == 'readBalance':
        result = crm.read_balance(data)
    elif method == 'addBalance':
        result = crm.add_balance(data)

    return result


def save_hook(data: dict):
    """
    Records the received hook.
    """
    hook = Hook()
    hook.body = json.dumps(data, ensure_ascii=False, indent=4)
    db.session.add(hook)
    db.session.commit()


def complete_hook(hook_id: int):
    """
    Mark the hook as completed.
    """
    hook = Hook.query.get_or_404(hook_id)
    if hook:
        hook.complete = True
        db.session.add(hook)
        db.session.commit()
        return {'success': True}


def rename_cts(data: dict):
    """
    Renames elements of cardTracks.

    Example: "1" to "ct_1".
    """
    if 'customer' in data and 'cardTracks' in data['customer']:
        cts_org = data['customer']['cardTracks']
        cts_new = dict()
        for ct in cts_org.keys():
            cts_new[f'ct_{ct}'] = cts_org[ct]
        data['customer']['cardTracks'] = cts_new
