# 🎯 Topic: 

-  🔸 What is an ORM and why we use it
-  🔸 SQLAlchemy setup with SQLite
-  🔸 Creating models that map to database tables
-  🔸 Building CRUD operations with FastAPI + DB integration

Challenge -  ✅ Build a Book Management API using:
- SQLAlchemy as ORM
- SQLite as backend
- Fully integrated with existing FastAPI endpoints
- No more in-memory dictionaries — this is now a persistent app! ✅

```
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from typing import List

# ------------------ DATABASE SETUP ------------------
DATABASE_URL = "sqlite:///./books.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

# ------------------ SQLAlchemy MODEL ------------------
class BookModel(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=False)

# ------------------ Pydantic SCHEMA ------------------
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

    class Config:
        orm_mode = True

# ------------------ CREATE TABLE ------------------
Base.metadata.create_all(bind=engine)

# ------------------ FASTAPI APP ------------------
app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------ ROUTES ------------------

@app.get("/books", response_model=List[Book])
def read_books(db: Session = Depends(get_db)):
    return db.query(BookModel).all()

@app.get("/books/{book_id}", response_model=Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/books", response_model=Book)
def create_book(book: Book, db: Session = Depends(get_db)):
    existing = db.query(BookModel).filter(BookModel.id == book.id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Book ID already exists")
    db_book = BookModel(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated: Book, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    book.title = updated.title
    book.author = updated.author
    book.year = updated.year
    db.commit()
    return book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}

```

ORMs like SQLAlchemy are super useful in real-world apps — especially in domains like:
**📚 Retail Inventory Management
 📖 Bookstore Applications
 👤 Customer Profiles & Orders
 📊 Dashboard & Reports
**
I went from memory-based lists ➡️ to full-blown database integration.
 The Book API now has a brain (FastAPI) and memory (SQLite). 🧠💾
Next up: Add relationships and maybe even JWT-authentication 👀

