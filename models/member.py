from . import db

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    outstanding_debt = db.Column(db.Float, default=0.0)

    def __init__(self, name, email):
        self.name = name
        self.email = email
