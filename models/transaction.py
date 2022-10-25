from sqlalchemy import Table,Column, Boolean, Column, ForeignKey, Integer, String
from config.db import meta,engine

transactions = Table(
    'transactions',meta,
    Column('id',Integer,primary_key=True),
    Column('book_id',Integer),
    Column('user_id',Integer),
    Column('book_name',String(225)),
    Column('borrowed_by',String(225)),
    Column('returned',Boolean)
)

meta.create_all(engine)