from fastapi import FastAPI
from backend.services.book_service import get_books
app=FastAPI()

@app.get("/")
def root():
    return{"message":"Amazon fast API"}

@app.get("/books")
def books():
    return get_books()

