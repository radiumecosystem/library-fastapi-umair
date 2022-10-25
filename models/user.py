from sqlalchemy import Table,Column, Boolean, Column, ForeignKey, Integer, String
from config.db import meta,engine

users = Table(
    'users',meta,
    Column('id',Integer,primary_key=True),
    Column('name',String(225)),
    Column('phone',String(225)),
    Column('isadmin',Boolean),
    Column('email',String(225))
)

meta.create_all(engine)