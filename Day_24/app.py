from flask import Flask, render_template
from dataclasses import dataclass

app = Flask(__name__)

# Dataclass to represent a book
@dataclass
class LibraryBook:
    id: int
    title: str
    author: str
    isbn: str
    publication_year: int

    def display(self):
        return f"{self.title} by {self.author} ({self.publication_year})"

# Sample book data
books = [
    LibraryBook(1, "Python Crash Course", "Eric Matthes", "978-1593276034", 2015),
    LibraryBook(2, "Fluent Python", "Luciano Ramalho", "978-1491946008", 2015),
    LibraryBook(3, "Clean Code", "Robert C. Martin", "978-0132350884", 2008)
]

# Homepage route - list of books
@app.route('/')
def home():
    return render_template("index.html", books=books)

# Detail route - show book by ID
@app.route('/book/<int:book_id>')
def book_detail(book_id):
    book = next((b for b in books if b.id == book_id), None)
    return render_template("book_detail.html", book=book)

if __name__ == "__main__":
    app.run(debug=True)
