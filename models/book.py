from . import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    author = db.Column(db.String(100))
    isbn = db.Column(db.String(30))
    publisher = db.Column(db.String(100))
    pages = db.Column(db.Integer)
    stock = db.Column(db.Integer)

    def __init__(self, title, author, isbn, publisher, pages, stock):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publisher = publisher
        self.pages = pages
        self.stock = stock
