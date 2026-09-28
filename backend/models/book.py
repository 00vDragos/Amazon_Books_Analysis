from pydantic import BaseModel, Field
from typing import Annotated
class Book(BaseModel):
    name: str = Field(alias='Name')
    author: str 
    user_rating: float
    reviews: int
    price: int
    year: int 
    genre: str 

