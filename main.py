from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

class Book(BaseModel):
    title: str
    author: str




books = [
    {
    "id": 1,
    "title": "Book_1",
    "author": "Author_1"
    },
    {
    "id": 2,
    "title": "Book_2",
    "author": "Author_2"
    }
]

@app.get("/books", tags=["books📚"])
def read_books():
    return books

@app.get("/books/{book_id}", tags=["books📚"])
def get_book(book_id:int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404)


@app.post("/books", tags=["books📚"])
def post_book(book: Book):
    books.append({
        "id": len(books) + 1,
        "title": book.title,
        "author": book.author
    })
    return books[-1]