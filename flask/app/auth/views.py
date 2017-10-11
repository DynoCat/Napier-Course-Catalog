from main import app, db, login_manager
from .forms import LoginForm
from .models import User

import flask
import flask_login

from flask import flash, redirect

@app.route('/account/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        userObj = User()
        user = userObj.get_by_email(email)
        if user and user.check_password(form.password.data):
            flask_login.login_user(user)
            flash("You have logged in as %s" % email)
            return flask.redirect(flask.url_for('homepage'))
        else:
            form.errors['global'] = ['Invalid credentials']
    return flask.render_template('login.html',
            form=form)

@app.route('/logout', methods=['GET', 'POST'])
@flask_login.login_required
def logout():
    flask_login.logout_user()
    flash("You have logged out")
    return redirect('/login')
