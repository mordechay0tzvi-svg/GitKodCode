from fastapi import FastAPI, Body, HTTPException, Query
import db
import uvicorn
from pydantic import BaseModel

class Soldier(BaseModel):
    name:str
    ranking:str
    unit:str
    active:bool
    

app = FastAPI()

# @app.post("/setup")
# def run_setup():
#     return {"status": "setup triggered"}

# @app.get("/schema")
# def get_schema():
#     columns = db.get_schema()
#     return {"columns": columns}

@app.get("/all-soldiers")
def get_all_soldiers():
    return {"soldiers": db.get_all()}

@app.get("/soldiers")
def get_soldiers(rank:str|None=Query(default=None), sort:str=Query(default="asc")):
    if rank:
        return {"soldiers":db.get_by_rank(rank)}
    return {"soldiers":db.get_active(sort)}

@app.post("/create")
def add_soldier(data:Soldier):
    data = data.model_dump()
    new_id = db.create(**data)
    return {"id":new_id, "message":"soldier created"}

@app.get("/soldiers/ranked")
def names_and_rankings():
    return {"soldiers":db.get_names_and_ranks()}

@app.get("/soldiers/units")
def list_units():
    return {"units": db.distinct_units()}

@app.get("/soldiers/search")
def search(name:str=Query(...)):
    return {"soldiers": db.search_by_name(name)}

@app.put("/soldiers/{id}")
def edit_soldier(id: int, body: Soldier):
    data = body.model_dump(exclude_none=True)
    success = db.update(id, data)
    if not success:
        raise HTTPException(status_code=404, detail="Soldier not found")
    return {"message": "Updated"}

@app.delete("soldiers/{id}")
def delete_soldier(id):
    deleted = db.delete(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Soldier not found")
    return {"message": f"{deleted} Deleted"}

@app.get("/soldiers/{id}")
def get_soldier(id:int):
    soldier = db.get_by_id(id)
    if not soldier:
        raise HTTPException(status_code=404, detail="soldier not found")
    return soldier

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
