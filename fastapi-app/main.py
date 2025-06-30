
from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/slow")
def slow_endpoint():
    time.sleep(2)
    return {"message": "Slow endpoint done."}
