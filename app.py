from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SECRET_KEY"] = "tujestwpisanykod"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    authors = db.relationship('Author', secondary='book_author', backref=db.backref('books', lazy='dynamic'))
    borrowed = db.relationship('Borrow', backref='book', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'authors': [author.name for author in self.authors],
            'borrowed': [borrow.returned for borrow in self.borrowed]
        }

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class BookAuthor(db.Model):
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), primary_key=True)

class Borrow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    returned = db.Column(db.Boolean, default=False)

@app.route("/books", methods=["GET"])
def get_all_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])