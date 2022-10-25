from pydantic import BaseModel
class Transaction(BaseModel):
    book_id:int
    user_id:int
    book_name:str
    borrowed_by:str
    returned:bool