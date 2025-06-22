# 🎯 Topic: 

- 🔹 Understanding RESTful architecture
- 🔹 Creating API endpoints using GET, POST, PUT, DELETE
- 🔹 Handling data with Pydantic models
- 🔹 Returning structured JSON responses

Challenge -  ✅ 𝗕𝘂𝗶𝗹𝗱 𝗮 𝗙𝗮𝘀𝘁𝗔𝗣𝗜 𝗮𝗽𝗽𝗹𝗶𝗰𝗮𝘁𝗶𝗼𝗻 𝘁𝗼 𝗺𝗮𝗻𝗮𝗴𝗲 𝗮 𝗹𝗶𝗯𝗿𝗮𝗿𝘆 𝗼𝗳 𝗯𝗼𝗼𝗸𝘀:
- GET → fetch all books
- POST → add a new book
- PUT → update book info
- DELETE → remove a book

```
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Pydantic model
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

# In-memory list of books with 5 preloaded items
library: List[Book] = [
    Book(id=1, title="Python Basics", author="Ravi Sharma", year=2020),
    Book(id=2, title="Flask Web Development", author="Meera Joshi", year=2018),
    Book(id=3, title="Data Science with Python", author="Amit Verma", year=2021),
    Book(id=4, title="Machine Learning", author="Anjali Singh", year=2022),
    Book(id=5, title="FastAPI for Beginners", author="Krushna Nayak", year=2024)
]

# GET all books
@app.get("/books", response_model=List[Book])
def get_books():
    return library

# GET a book by ID
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in library:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# POST a new book
@app.post("/books", response_model=Book)
def create_book(book: Book):
    for existing in library:
        if existing.id == book.id:
            raise HTTPException(status_code=400, detail="Book ID already exists")
    library.append(book)
    return book

# PUT (update) an existing book
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    for i, book in enumerate(library):
        if book.id == book_id:
            library[i] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

# DELETE a book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(library):
        if book.id == book_id:
            del library[i]
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
```

📌 𝗞𝗲𝘆 𝗟𝗲𝗮𝗿𝗻𝗶𝗻𝗴:

FastAPI makes it incredibly easy to develop and document REST APIs — with type safety, speed, and structure.
 This is a core skill in building:
 Backend systems for retail
 Inventory management tools
 Customer portals
 Product catalogs and dashboards

 REST APIs are the connective tissue between frontends, databases, and third-party systems.

If you want to build web apps, mobile apps, or automate backend services — start with REST, start with FastAPI. 💥

#FastAPI #Python #BackendDevelopment #RESTAPI #30DaysOfPython #KrushnaLearnsPython #Pydantic #BookAPI #LearningInPublic #BuildInPublic #RetailTech #PythonChallenge



