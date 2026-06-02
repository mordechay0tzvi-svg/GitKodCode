import fastapi
import uvicorn
import json
import os
from fastapi import Body
FILE_NAME = "names.json"

app = fastapi.FastAPI()

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([{"name": "name", "id": "id"}], f)


def load_names():
    with open(FILE_NAME, 'r') as f:
        return json.load(f)
    
def save_names(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f)


@app.put("/names/register")
def add_name(item: dict):
    names = load_names()
    names.append(item)
    save_names(names)
    return {"added":item}

@app.get("/names")
def get_names():
    names = load_names()
    return names
    
@app.get("/names/{identity}")
def get_name(identity:str):
    names = load_names()
    for name in names:
        if name['id'] == identity or name['name'] == identity :
            return {"found":name}
    return {"message":"couldn't find"}
            
@app.delete("/names/{identity}")
def delete_number(identity:str):
    names = load_names()
    for name in names:
        if name['id'] == identity or name['name'] == identity :
            names.remove(name)
            save_names(names)
            return {"message": "deleted"}
    return {"error": "not found"}



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5686)