from fastapi import FastAPI
from database import engine,Base
import models

app = FastAPI(title = "Personal Finance Management API")
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message":"Personal Finance Management Api"}

@app.get("/about")
def about():
    return {"message":"Shivam Codes"}