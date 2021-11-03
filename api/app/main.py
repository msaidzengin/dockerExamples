from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def read_root():
    return "API çalışıyor"

@app.get('/random')
def deneme():
    return str(random.randint(1, 100))
