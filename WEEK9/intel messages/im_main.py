import uvicorn
from fastapi import FastAPI, Body, HTTPException
import im_db
from pydantic import BaseModel

class Message(BaseModel):
    unit:str
    classification:str
    source:str
    content:str

app = FastAPI()

@app.post("/setup")
def setup():
    return {"status": "ok", "table": "intelmessages"}

@app.get("/schema")
def schema():
    return im_db.get_schema()

@app.get("/messages")
def messages():
    return {"messages": im_db.get_all_messages()}

@app.post("/messages")
def add_message(data:Message):
    data = data.model_dump()
    if data["classification"] not in im_db.is_valid_classification():
        raise HTTPException(status_code=400, detail="not valid classification status")
    return {"message":im_db.add_message(**data)}

@app.get("/messages/{id}")
def get_by_id(id:int):
    if not im_db.get_message(id):
        raise HTTPException(status_code=404, detail="message not found")
    return im_db.get_message(id)

@app.delete("/messages/{id}")
def delete(id:int):
    deleted = im_db.delete_message(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="message not found")
    return {deleted:"deleted"}

@app.put("/messages/{id}")
def update(id:int, data:dict):
    if data["classification"] not in im_db.is_valid_classification():
        raise HTTPException(status_code=400, detail="not valid classification status")
    updated = im_db.update_message(id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="message not found")
    return {updated:"updaated"}

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)

