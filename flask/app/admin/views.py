from main import app, db
from .models import LocationPage
from .forms import LocationPageForm

import flask
import flask_login

from flask import flash, redirect

@app.route('/admin/dashboard', methods=['GET', 'POST'])
@flask_login.login_required
def admin_dashboard():
    return flask.render_template('admin/dashboard.html')

@app.route('/admin/locations', methods=['GET'])
@flask_login.login_required
def admin_locations():
    locations = LocationPage.query.all()
    return flask.render_template('admin/location-page.html',
                                locations=locations)

@app.route('/admin/locations/new', methods=['GET', 'POST'])
@flask_login.login_required
def admin_locations_new():
    form = LocationPageForm()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data

        page = LocationPage(name=name,
                            description=description,
                           )
        db.session.add(page)
        db.session.commit()
        return flask.redirect('/admin/locations')
    return flask.render_template('admin/location-page-edit.html',
                                form=form)
