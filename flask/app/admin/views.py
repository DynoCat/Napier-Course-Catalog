from main import app, db, login_manager

import flask

from flask import flash, redirect

@app.route('/admin/dashboard', methods=['GET', 'POST'])
def admin_dashboard():
    return flask.render_template('admin/dashboard.html')
