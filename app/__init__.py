from flask import Flask
import os

def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello/')
    def hello():
        return 'Hello, world!'

    from . import env
    app.register_blueprint(env.bp)
    env.init_app(app)


    return app