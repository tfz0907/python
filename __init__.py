from flask import Flask
from App.exts import init_exts
from App.settings import env
from App.views import init_blue
from App.urls import *

def create_app(envinfo='develop'):
    app=Flask(__name__)

    app.config.from_object(env.get(envinfo))

    init_exts(app)
    init_blue(app)

    return app
