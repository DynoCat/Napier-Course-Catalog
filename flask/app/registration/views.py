from main import app, db
from flask import Flask, request, render_template, flash, redirect, url_for, session, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators

from .models import UserDetails
from .forms import RegisterForm

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():

        user = UserDetails(
            name = form.name.data,
            username = form.username.data,
            email = form.email.data,
            password = form.password.data
            #register_date='date'
        )

        db.session.add(user)
        db.session.commit()

        # Create cursor
        #cur = mysql.connection.cursor()

        # Execute query
        #cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))

        # Commit to DB
        #mysql.connection.commit()

        # Close connection
        #cur.close()

        flash('You are now registered and can log in', 'success')

        #redirect(url_for('index'))
        return redirect(url_for('successfully_registered'))
    return render_template('register.html', form=form)

@app.route('/successfully_registered', methods=['GET'])
def successfully_registered():
    return render_template('successfully_registered.html')
