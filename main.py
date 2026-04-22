from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/greet")
def greet():
    return {"message": "Hello"}

@app.get("/number/{max_number}")
def number(max_number:int):
    return {
        "max number":max_number,
        "random number" : random.randint(1,max_number)
    }