from sqlalchemy import Table,Column, Boolean, Column, ForeignKey, Integer, String
from config.db import meta,engine

books = Table(
    'books',meta,
    Column('id',Integer,primary_key=True),
    Column('name',String(225)),
    Column('author',String(225)),
    Column('isborrowed',Boolean)
)

meta.create_all(engine)