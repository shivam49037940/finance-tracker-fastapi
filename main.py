from fastapi import FastAPI

app = FastAPI(title = "Personal Finance Management API")

@app.get("/")
def root():
    return {"message":"Personal Finance Management Api"}

@app.get("/about")
def about():
    return {"message":"Shivam Codes"}