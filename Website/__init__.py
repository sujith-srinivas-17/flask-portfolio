from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']= '70cf1410-abf5-4bf4-b07e-8f0163f1bf13'
    from .home import home
    app.register_blueprint(home, url_prefix = '/')
    return app