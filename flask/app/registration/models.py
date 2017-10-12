from main import db

class UserDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    username = db.Column(db.String(30))
    password = db.Column(db.String(100))
    #register_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
