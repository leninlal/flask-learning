import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'passme'
    SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@localhost/flasky" % (MYSQL_USER,MYSQL_PASSWORD)
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

class TestingConfig(Config):
    TESTING = True
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '1'
    SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@localhost/flasky" % (MYSQL_USER,MYSQL_PASSWORD)

class ProductionConfig(Config):
    MYSQL_USER = ''
    MYSQL_PASSWORD = ''
    SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@localhost/flasky" % (MYSQL_USER,MYSQL_PASSWORD)

config = {
'development': DevelopmentConfig,
'testing': TestingConfig,
'production': ProductionConfig,
'default': DevelopmentConfig
}