from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_mail import Mail
from flask_cache import Cache

db=SQLAlchemy()
migrate=Migrate()
api=Api()
mail=Mail()
cache=Cache(config={
    'CACHE_TYPE':'simple'
})

def init_exts(app):
    db.init_app(app)
    migrate.init_app(app,db)
    api.init_app(app)
    mail.init_app(app)
    cache.init_app(app)ex
