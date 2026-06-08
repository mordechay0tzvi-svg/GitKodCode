from fastapi import FastAPI, Body
import db
import uvicorn
from pydantic import BaseModel

class Soldier(BaseModel):
    name:str
    ranking:str
    unit:str
    active:bool
    

app = FastAPI()
@app.post("/setup")
def run_setup():
    return {"status": "setup triggered"}

@app.get("/schema")
def get_schema():
    columns = db.get_schema()
    return {"columns": columns}

@app.get("/soldiers")
def get_all_soldiers():
    return db.get_all()

@app.get("/soldiers/{id}")
def get_soldier(id:int):
    return db.get_by_id(id)

@app.post("/create")
def add_soldier(data:Soldier):
    data = data.model_dump()
    return db.create(**data)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
