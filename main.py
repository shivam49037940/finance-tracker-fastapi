from fastapi import FastAPI
from database import engine,Base
import models
from router import auth

app = FastAPI(title = "Personal Finance Management API")
app.include_router(auth.router)
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message":"Personal Finance Management Api"}

@app.get("/about")
def about():
    return {"message":"Shivam Codes"}