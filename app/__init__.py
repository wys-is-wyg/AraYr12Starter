from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.secret_key = 'SECRET_KEY'
    router(app)

    return app


def router(app):

    from app.views import home
    app.register_blueprint(home.bp)