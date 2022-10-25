from fastapi import APIRouter
from config.db import conn
from models.index import transactions,users,books
from schemas.index import Transaction,User,Book
user = APIRouter()

@user.get("/")
async def welcome():
    return "Welcome to Library Management FastAPI's developed by Umair"

@user.get("/users")
async def all_users():
    return conn.execute(users.select()).fetchall()

@user.get("/users/{userid}")
async def get_user(userid):
    return conn.execute(users.select().where(users.c.id==userid)).first()

@user.post("/createuser")
async def create_user(user:User):
     conn.execute(users.insert().values(
        name=user.name,
        email=user.email,
        phone=user.phone,
        isadmin=user.isadmin 
    ))
     return conn.execute(users.select()).fetchall()

@user.put("/edituser/{userid}")
async def edit_user(user:User,userid:int):
      conn.execute(users.update().values(
        name=user.name,
        email=user.email,
        phone=user.phone,
        isadmin=user.isadmin 
      ).where(users.c.id==userid))
      return conn.execute(users.select()).fetchall()

@user.delete("/deleteuser/{userid}")
async def delete_user(userid:int):
     conn.execute(users.delete().where(users.c.id==userid))
     return conn.execute(users.select()).fetchall()


