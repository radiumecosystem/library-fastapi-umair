from fastapi import APIRouter
from config.db import conn
from models.index import transactions,users,books
from schemas.index import Transaction,User,Book
book = APIRouter()

@book.get("/books")
async def View_all_book():
    return conn.execute(books.select()).fetchall()

@book.get("/books/{bookid}")
async def search_book(bookid):
    return conn.execute(books.select().where(books.c.id==bookid)).first()

@book.post("/addbook/{userid}")
async def add_book_only_admin(book:Book,userid:int):
   admin = conn.execute(users.select().where(users.c.id==userid)).first().isadmin
   if admin:
      conn.execute(books.insert().values(
        name=book.name,
        author=book.author,
        isborrowed=False 
       ))
      return conn.execute(books.select()).fetchall()
   else:
      return "only admin can add book"
     
     
@book.put("/editbook/{userid}/{bookid}")
async def edit_book_only_admin(book:Book,bookid:int,userid:int):
   admin = conn.execute(users.select().where(users.c.id==userid)).first().isadmin
   if admin:
      conn.execute(books.update().values(
        name=book.name,
        author=book.author 
      ).where(books.c.id==bookid))
      return conn.execute(books.select()).fetchall()
   else:
      return "only admin can edit book"
      
@book.delete("/deletebook/{userid}/{bookid}")
async def delete_book_only_admin(bookid:int,userid:int):
   admin = conn.execute(users.select().where(users.c.id==userid)).first().isadmin
   if admin:
     conn.execute(books.delete().where(books.c.id==bookid))
     return conn.execute(books.select()).fetchall()
   else:
      return "only admin can delete book"