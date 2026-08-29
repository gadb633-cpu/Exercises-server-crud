from fastapi import FastAPI
from pydantic import BaseModel
import json
from load_id import *

app = FastAPI()

@app.get("/grades")
def read_root():
    return load_db()

@app.get("/grades/{id}")
def read_root(id):
    print("type and id are:",type(id),id)
    return check_id(id)
