from flask import Flask
import os


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'rain3.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    print('Welcome to ' + app.config['VERSION'])

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello/')
    def hello():
        return 'Hello, world!'

    from app.controllers import db
    db.init_app(app)

    from app.views import env
    app.register_blueprint(env.bp)
    env.init_app(app)

    from app.views import target
    app.register_blueprint(target.bp)

    return app
