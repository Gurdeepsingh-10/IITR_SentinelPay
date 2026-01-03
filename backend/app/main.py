from fastapi import FastAPI
from app.routes import auth, transactions
from app.db.session import connect_db, disconnect_db

app = FastAPI()

app.include_router(auth.router)
app.include_router(transactions.router)

@app.on_event("startup")
async def startup():
    await connect_db()

@app.on_event("shutdown")
async def shutdown():
    await disconnect_db()
