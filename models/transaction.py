from . import db

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    type = db.Column(db.String(10))  # issue or return
    fee = db.Column(db.Float)

    def __init__(self, member_id, book_id, type, fee):
        self.member_id = member_id
        self.book_id = book_id
        self.type = type
        self.fee = fee
