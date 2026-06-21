from fastapi import FastAPI, Body, Query
import uvicorn
from intel_messages_dal import *
from pydantic import BaseModel


class Message(BaseModel):
    unit: str
    classification: str
    content: str
    source: str | None = None

mm = IntelMessagesDAL("localhost", "root", 3306, "secret", "soldiers_db")
app = FastAPI()

@app.get("/")
def greeting():
    return {"message":"welcome to intel messages"}

@app.get("/schema")
def get_schema():
    return mm.get_schema()

@app.get("/messages")
def get_messages(unit:str=Query(...),classification:str=Query(...)):
    return mm.get_all()
    return mm.get_by_unit(unit)
    return mm.get_by_unit_and_classification(unit, classification)

@app.get("/messages/units")
def get_units():
    return mm.get_distinct_units()

@app.get("messages/search")
def search(q:str=Query(...)):
    return mm.search_content(q)

@app.get("/messages/missing-source")
def no_source():
    return mm.get_missing_source()

@app.post("/messages")
def add_message(data:Message=Body(...)):
    return mm.create(**data)

@app.get("/messages/{message_id}")
def get_message(id:int):
    return mm.get_by_id(id)

@app.put("/messages/{message_id}")
def update_message(id:int, data:dict=Body(...)):
    return mm.update(id, data)

@app.delete("/messages/{message_id}")
def delete_message(id:int):
    return mm.delete(id)
    


