from flask import Blueprint, request
from app.controllers.db import get_db
from app.controllers.target import get_all_targets, set_many_targets, disable_many_targets

bp = Blueprint('target', __name__, url_prefix='/target')


@bp.route('/list/')
def list_targets():
    res = get_all_targets()
    res = filter(lambda x:x['enabled'] == True, res)

    return {'target': [{'id': x['id'],
                        'host': x['host'],
                        'port': x['port']} for x in res]}


@bp.route('/add/', methods=['POST'])
def add_targets():
    add, enable = set_many_targets(request.form['target'])

    return {'add': [str(x) for x in add],
            'enable': [str(x['info']) for x in enable]}


@bp.route('/disable/', methods=['POST'])
def disable_targets():
    done = disable_many_targets(request.form['target'])

    return {'disable': [str(x['info']) for x in done]}


