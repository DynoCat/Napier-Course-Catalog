from main import app, login_manager, db, flask_bcrypt

import flask_login

class User(flask_login.UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(60))

    def __init__(self, email=email, password=password):
        self.email = email
        self.password = password

    def check_password(self, password):
        if self.password and flask_bcrypt.check_password_hash(self.password, password):
            return True
        else:
            return False

    def get_by_email(self, email):
        user = User.query.filter_by(email=email).first()
        if user:
            self.email = user.email
            self.password = user.password
            self.id = user.id
            return self
        else:
            return None

@login_manager.user_loader
def user_loader(id):
    return User().query.get(int(id))
