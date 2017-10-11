from main import app, db
from .models import LocationPage

import flask
import flask_login

from flask import flash, redirect

@app.route('/admin/dashboard', methods=['GET', 'POST'])
@flask_login.login_required
def admin_dashboard():
    return flask.render_template('admin/dashboard.html')

@app.route('/admin/locations', methods=['GET', 'POST'])
@flask_login.login_required
def admin_locations():
    locations = LocationPage.query.all()
    return flask.render_template('admin/location-page.html',
                                locations=locations)
