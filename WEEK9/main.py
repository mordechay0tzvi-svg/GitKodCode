from fastapi import FastAPI, Body, HTTPException
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
    return {"soldiers": db.get_all()}

@app.get("/soldiers/{id}")
def get_soldier(id:int):
    soldier = db.get_by_id(id)
    if not soldier:
        raise HTTPException(status_code=404, detail="soldier not found")
    return soldier

@app.post("/create")
def add_soldier(data:Soldier):
    data = data.model_dump()
    new_id = db.create(**data)
    return {"id":new_id, "message":"soldier created"}

@app.delete("soldiers/{id}")
def delete_soldier(id):
    deleted = db.delete(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Soldier not found")
    return {"message": f"{deleted} Deleted"}

@app.put("/soldiers/{id}")
def edit_soldier(soldier_id: int, body: SoldierIn):
    data = body.model_dump(exclude_none=True)
    success = db.update(soldier_id, data)
    if not success:
        raise HTTPException(status_code=404, detail="Soldier not found")
    return {"message": "Updated"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
