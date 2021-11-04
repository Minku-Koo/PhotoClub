# flask create app
# Project Start : 20210923

from flask import Flask
from .views import views
import os

def create_app():
    app = Flask(__name__)
    app.register_blueprint(views)
    app.secret_key = "this1sCjUUP0t0C1bu"
    app.jinja_env.add_extension("jinja2.ext.loopcontrols")
    
    return app