#!/usr/bin/env python

import os
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from flask_login import LoginManager

app = FlaskAPI(__name__)

app.config.from_object('config.' + os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

flask_bcrypt = Bcrypt(app)

from views.api import *
from views.templates import *

from auth import views

@app.cli.command()
def initdb():
    db.create_all()

    db.create_all()

@app.cli.command()
def addadmin():
    from auth.models import User
    password = flask_bcrypt.generate_password_hash('pass')
    user = User(email='admin@example.com', password=password)
    db.session.add(user)
    db.session.commit()

@app.cli.command()
def test():
    import pytest
    currentPath = os.path.dirname(os.path.abspath(__file__))
    rv = pytest.main([currentPath, '--ignore=env', '--ignore=node_modules',
                      '--verbose'])
    exit(rv)

if __name__=='__main__':
    app.run()
