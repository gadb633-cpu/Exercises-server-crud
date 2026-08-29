import json
from fastapi import FastAPI ,HTTPException
def load_db():
    with open('db.json','r', encoding='utf-8') as file:
        data = json.load(file)
    return data    
def check_id(id):
    id = int(id)
    data_grades = load_db()
    for grade in data_grades:
        if grade["id"] == id:
            return 
        else:
            raise HTTPException(status_code=404, detail="Item not found")         