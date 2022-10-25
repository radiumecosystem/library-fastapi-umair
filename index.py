from fastapi import FastAPI
from routes.index import user,book,transaction
app = FastAPI()

app.include_router(user)
app.include_router(book)
app.include_router(transaction)