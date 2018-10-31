import os


class Config(object):
    # noinspection SpellCheckingInspection
    # import secrets
    # secrets.token_hex(16)
    SECRET_KEY = 'bcaa436189daf75374ecebec4a652522'
    # The three slashes means a relative path so the file will next to the script
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
