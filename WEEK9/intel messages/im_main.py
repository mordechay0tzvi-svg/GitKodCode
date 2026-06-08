import uvicorn
from fastapi import FastAPI
import im_db


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



if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)

