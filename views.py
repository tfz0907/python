from flask import Blueprint,render_template
from App.models import *
blue=Blueprint('blue',__name__)

def init_blue(app):
    app.register_blueprint(blue)

@blue.route('/index/')
def index():
    return render_template('index.html')
