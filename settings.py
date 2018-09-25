import os

BASE_DIR=os.path.join(os.path.dirname(os.path.abspath(__file__)))


def get_db_uri(dbinfo):
    db=dbinfo.get('DB')
    driver=dbinfo.get('DRIVER')
    user=dbinfo.get('USER')
    password=dbinfo.get('PASSWORD')
    host=dbinfo.get('HOST')
    port=dbinfo.get('PORT')
    name=dbinfo.get('NAME')
    return "{}+{}://{}:{}@{}:{}/{}".format(db,driver,user,password,host,port,name)

class Config:
    DEBUG=False
    TESTING=False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '110'

class DevelopConfig(Config):
    DEBUG = True
    ENV = "development"  # 开发环境

    # 邮箱配置
    MAIL_SERVER = 'smtp.163.com'  # 邮箱服务器
    MAIL_USERNAME = 'tfzv58@163.com'  # 邮箱用户名
    MAIL_PASSWORD = 'tfzv58'  # 授权码

    # 数据库配置
    DATABASE = {
        'DB': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'rock1204',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'tpp_copy',
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)



# 测试环境
class TestingConfig(Config):
    TESTING = True

    DATABASE = {
        'DB': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'rock1204',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'tpp_copy',
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


# 生产环境
class ProductConfig(Config):
    DEBUG = False

    DATABASE = {
        'DB': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'rock1204',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'tpp_copy',
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


env = {
    'develop': DevelopConfig,
    'test': TestingConfig,
    'product': ProductConfig,
}
