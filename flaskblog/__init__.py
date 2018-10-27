from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# noinspection SpellCheckingInspection
# import secrets
# secrets.token_hex(16)
app.config['SECRET_KEY'] = 'bcaa436189daf75374ecebec4a652522'
# The three slashes means a relative path so the file will next to the script
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # same as the value that would be passed into url_for
login_manager.login_message_category = 'info'

# This import is here to avoid circular imports.  If they were at the top of the file routes.py
# would try to import app before it was initialized.
from flaskblog import routes