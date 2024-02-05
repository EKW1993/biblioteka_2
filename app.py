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
@app.route("/books", methods=["GET"])
def get_all_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = Book.query.get(book_id)
    if book:
        return jsonify(book.to_dict())
    else:
        return jsonify({"error": "Book not found"}), 404
    
@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()
    authors = []
    if 'authors' in data:
        author_names = data.pop('authors')
        for author_name in author_names:
            author = Author.query.filter_by(name=author_name).first()
            if not author:
                author = Author(name=author_name)
                db.session.add(author)
            authors.append(author)
    book = Book(**data)
    book.authors = authors
    db.session.add(book)
    db.session.commit()
    return jsonify({"message": "Book created successfully"})    

@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json()
    book = Book.query.get(book_id)
    if book:
        authors = []
        if 'authors' in data:
            author_names = data.pop('authors')
            for author_name in author_names:
                author = Author.query.filter_by(name=author_name).first()
                if not author:
                    author = Author(name=author_name)
                    db.session.add(author)
                authors.append(author)
        book.title = data.get('title', book.title)
        book.authors = authors
        db.session.commit()
        return jsonify({"message": "Book updated successfully"})
    else:
        return jsonify({"error": "Book not found"}), 404
    
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": "Book deleted successfully"})
    else:
        return jsonify({"error": "Book not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)