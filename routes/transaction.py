from unicodedata import name
from fastapi import APIRouter
from sqlalchemy import false, true
from config.db import conn
from models.index import transactions,users,books
from schemas.index import Transaction,User,Book
transaction = APIRouter()

@transaction.get("/transactions")
async def all_transaction():
    return conn.execute(transactions.select()).fetchall()

@transaction.post("/borrow/{bookid}/{userid}")
async def borrow_book(bookid:int,userid:int):
    borrowed = conn.execute(books.select().where(books.c.id==bookid)).first().isborrowed
    if borrowed:
        return "already borrowed by someone else"
    else:
        conn.execute(books.update().values(
        isborrowed=True
        ).where(books.c.id==bookid))
        conn.execute(transactions.insert().values(
        book_id=bookid,
        user_id=userid,
        book_name=conn.execute(books.select().where(books.c.id==bookid)).first().name,
        borrowed_by=conn.execute(users.select().where(users.c.id==userid)).first().name,
        returned=False 
        ))
        return conn.execute(transactions.select()).fetchall()
       

@transaction.put("/return/{transactionid}")
async def return_book(transactionid:int):
     conn.execute(books.update().values(
        isborrowed=False
        ).where(books.c.id==conn.execute(transactions.select().where(transactions.c.id==transactionid)).first().book_id))
     conn.execute(transactions.update().values(
        returned=True 
    ).where(transactions.c.id==transactionid))
     return conn.execute(transactions.select()).fetchall()