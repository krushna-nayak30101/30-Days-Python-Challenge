# 🎯 Topic: 
-    🔹 How to install and set up a Flask project
-    🔹 Creating routes to control page navigation
-    🔹 Building HTML templates using Jinja2
-    🔹 Linking Python backend logic with the frontend using @dataclass

Challenge -Build a minimal library system to manage book records using @dataclass for structure and Flask for the web interface.

```
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
```

  🔍 Key Learnings:

- @dataclass keeps Python data models clean and minimal
- Flask + Jinja2 makes it easy to build dynamic web pages
- Combining logic and presentation helps understand full-stack basics

📚 A fun, functional way to bridge backend Python with simple frontend templating.
Let me know if you want the full code or ZIP — happy to share!

#Python #Flask #Dataclass #WebDevelopment #MiniProject #PythonProjects #30DaysOfCode #KrishnaLearns #Jinja2 #FullStackBasics
