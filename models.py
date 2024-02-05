from app import db

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