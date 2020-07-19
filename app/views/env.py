from flask import Blueprint, redirect, url_for, current_app
from flask.cli import with_appcontext
from app.controllers.db import init_db
import platform, click, os

bp = Blueprint('env', __name__, url_prefix='/env')


@bp.route('/python/')
def get_python_version():
    return platform.python_version()


@bp.route('/platform/')
def get_platform_info():
    return platform.platform()


@click.command('freeze-packages')
@with_appcontext
def freeze_packages_command():
    path = os.path.join(current_app.root_path, 'static', 'env', 'freeze.txt')
    click.echo(f'saving packages to {path}...')
    os.system(f'pip freeze > {path}')


def init_app(app):
    app.cli.add_command(freeze_packages_command)


@bp.route('/packages/')
def get_installed_packages():
    return redirect(url_for('static', filename='/env/freeze.txt'))


@bp.route('/clean/')
def clean_database():
    init_db()

    return 'OK'