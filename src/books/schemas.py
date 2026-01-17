from pydantic import BaseModel
from typing import Optional

##Response model or payload structure
class Book(BaseModel):
    id : int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
    
    
##Updated Response model or Updated payload structure
class BookUpdateModel(BaseModel):
    title:Optional[str]=None
    author:Optional[str]=None
    publisher:Optional[str]=None
    page_count:Optional[int]=None
    language:Optional[str]=None