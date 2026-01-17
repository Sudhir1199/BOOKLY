from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from typing import List
from src.books.book_data import books
from src.books.schemas import Book, BookUpdateModel
from fastapi import APIRouter

book_router = APIRouter()

#Getting all book
@book_router.get('/', response_model=List[Book])
async def get_all_books():
    return books

#saving the book
@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data:Book)-> dict:
    new_book = book_data.model_dump ()
    
    books.append(new_book)
    return new_book

#getting book by id
@book_router.get("/{book_id}")
async def get_book(book_id:int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book not found")
        

#updating the book by id
@book_router.patch("/{book_id}")
async def update_book(book_id:int, book_updated_data:BookUpdateModel) -> dict:
    
    for book in books:
        if book['id'] == book_id:
            
            update_data = book_updated_data.model_dump(exclude_unset=True)
            
            for key,value in update_data.items():
                book[key] = value
            return book
        
 ## incase we havnt found our existing book to update then throw exception
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found!!")
    

@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int): ## as we dont want to return anything so whats the use of dict
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            
            return{}
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
