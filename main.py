from fastapi import FastAPI, Header
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Message":"Hello"}


@app.get("/greet")
async def greet_name(name:Optional[str]="User", age:int = 0)->dict:
    return{"message":f"Hello {name}", "age":age}
## in above as we havent provide the parameter which the url asked so we can resolve it using query parameter ex "/greet?name=sudhir"
## in above if user dont give name which is optional then in that case it showing the default value as "User"
## url-> http://127.0.0.1:8000/greet?name=sudhir&age=25
## so here is the path parmeter aand query pamater(?)



class BookCreateMOdel(BaseModel):
    title : str
    author : str
    
    

# Pydantic is a data validation and parsing library that converts raw data into typed Python objects.
# BaseModel defines the schema and automatically validates, parses, and serializes data.


@app.post("/create_book")
async def create_book(book_data:BookCreateMOdel):
    return{
        "title":book_data.title,
        "author":book_data.author
    }

## so here comes the concept of validation and serialization 
## validation-> validating the client request in server then hit the database 
## serialization-> after validating, filtering the data and conveting it to JSON reponse, given to client from server

@app.get("/get_headers")
async def get_header(
    accept:str = Header(None), 
    content_type:str = Header(None)
    
):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content_Type"] = content_type
    return request_headers
