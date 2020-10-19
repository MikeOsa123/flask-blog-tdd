'''
All config infromation for each environment needed for the application to run
'''

import os
from dotenv import load_dotenv

# root directory of the application
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class BaseConfig(object):
    """Default BaseConfig. Use this for development environments."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'random-key-string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['ADMINS']
    WTF_CSRF_ENABLED = True

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'dev.db')

class TestingConfig(BaseConfig):
    """BaseConfigurations used for Testing."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-means-nothing'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'test.db')
    BCRYPT_LOG_ROUNDS = 4
    WTF_CSRF_ENABLED = False

class ProductionConfig(BaseConfig):
    """BaseConfigurations to be used in Production."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Who-let-the-dogs-out?'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'prod.db')

class StagingConfig(BaseConfig):
    """BaseConfigurations to be used in Production."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Here-we-go-again?'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('STAGING_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'stage.db')

config = {
    'testing': TestingConfig,
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'staging' : StagingConfig,

    'default' : DevelopmentConfig
}