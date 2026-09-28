from backend.repositories.book_repository import load_books
from backend.models import Book



def get_books():
    df=load_books()
    records=df.to_dict(orient="records")
    books=[Book(**record) for record in records]
    return books


