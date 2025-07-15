from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from models import db, Book, Member, Transaction
import requests

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    return redirect(url_for('books'))

@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        isbn = request.form['isbn']
        publisher = request.form['publisher']
        pages = int(request.form['pages'])
        stock = int(request.form['stock'])
        book = Book(title, author, isbn, publisher, pages, stock)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('books'))
    books = Book.query.all()
    return render_template('books.html', books=books)

@app.route('/import_books', methods=['POST'])
def import_books():
    import requests
    num_books = int(request.form.get('num_books', 20))
    title = request.form.get('title', '')
    author = request.form.get('author', '')
    publisher = request.form.get('publisher', '')
    page = request.form.get('page', 1)

    params = {
        'page': page,
        'title': title,
        'authors': author,
        'publisher': publisher
    }

    response = requests.get('https://frappe.io/api/method/frappe-library', params=params)
    if response.status_code != 200:
        flash('Failed to fetch books from Frappe API.')
        return redirect(url_for('books'))

    data = response.json()
    books_data = data.get('message', [])
    count = 0

    for book_data in books_data:
        if count >= num_books:
            break

        book_title = book_data.get('title', '').strip()
        book_author = book_data.get('authors', '').strip()

        # Only save books with title & author
        if not book_title or not book_author:
            continue

        new_book = Book(
            title = book_title,
            author = book_author,
            isbn = book_data.get('isbn') or '',
            publisher = book_data.get('publisher') or '',
            pages = int(book_data.get('num_pages') or 0),
            stock = 5
        )

        db.session.add(new_book)
        count += 1

    db.session.commit()
    flash(f"Imported {count} books from Frappe Library API!")
    return redirect(url_for('books'))

@app.route('/books/delete/<int:book_id>')
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for('books'))

@app.route('/members', methods=['GET', 'POST'])
def members():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        member = Member(name, email)
        db.session.add(member)
        db.session.commit()
        return redirect(url_for('members'))
    members = Member.query.all()
    return render_template('members.html', members=members)

@app.route('/members/delete/<int:member_id>')
def delete_member(member_id):
    member = Member.query.get(member_id)
    if member:
        db.session.delete(member)
        db.session.commit()
    return redirect(url_for('members'))

@app.route('/issue', methods=['GET', 'POST'])
def issue():
    books = Book.query.all()
    members = Member.query.all()
    if request.method == 'POST':
        member_id = request.form['member_id']
        book_id = request.form['book_id']
        member = Member.query.get(member_id)
        book = Book.query.get(book_id)

        if not book:
            flash('Book not found!')
            return redirect(url_for('issue'))
        if not member:
            flash('Member not found!')
            return redirect(url_for('issue'))
        if book.stock <= 0:
            flash('Book out of stock!')
            return redirect(url_for('issue'))
        if member.outstanding_debt > 500:
            flash('Outstanding debt exceeds Rs.500!')
            return redirect(url_for('issue'))

        book.stock -= 1
        txn = Transaction(member.id, book.id, 'issue', 0)
        db.session.add(txn)
        db.session.commit()
        return redirect(url_for('issue'))
    return render_template('issue.html', books=books, members=members)

@app.route('/return', methods=['GET', 'POST'])
def return_book():
    books = Book.query.all()
    members = Member.query.all()
    if request.method == 'POST':
        member_id = request.form['member_id']
        book_id = request.form['book_id']
        fee = float(request.form['fee'])
        member = Member.query.get(member_id)
        book = Book.query.get(book_id)

        if not book:
            flash('Book not found!')
            return redirect(url_for('return_book'))
        if not member:
            flash('Member not found!')
            return redirect(url_for('return_book'))

        book.stock += 1
        member.outstanding_debt += fee

        txn = Transaction(member.id, book.id, 'return', fee)
        db.session.add(txn)
        db.session.commit()
        return redirect(url_for('return_book'))
    return render_template('return.html', books=books, members=members)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
