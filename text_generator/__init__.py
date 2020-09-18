from flask import Flask
from .routes import generator
# 15. We need to import the modules in our init file for flask
# !!! Not needed
# from .model import *
# from .sample import *
# from .encoder import *

# 4. Explain how to initialize a flask app and talk about flask
# the settings file,  __name__ and config_file
def create_app(config_file='settings.py'):
    # EXPLAIN HOW WE NEED THE STATIC FOLDER FOR IMAGES (WALLEY IN THIS CASE)
    app = Flask(__name__, static_url_path = "/tmp", static_folder = "tmp")

    app.config.from_pyfile(config_file)
    # 6. Register blueprint explain
    app.register_blueprint(generator)
    return app

