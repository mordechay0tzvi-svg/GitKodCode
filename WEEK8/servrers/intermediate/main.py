from fastapi import FastAPI
import uvicorn
from datetime import datetime
app = FastAPI()

@app.get("/")
def initial_get():
    return  {"service": "my-api", "version": "1.0"}


@app.get("/users/admin")
def users_admin():
    return {"role": "admin", "access": "full"} 

@app.get("/users/{user_id}")
def user_id(user_id):
    return  {"user id": user_id, "name": "your_name_here", 'email': "your_email_here"}

@app.get("/calc/{a}/{op}/{b}")
def calc_op(a:int, op:str, b:int):
    try:
        if op == "add":
            r = a + b
            return {"operation": op, "result": r}
        elif op == "sub":
            r = a - b
            return {"operation": op, "result": r}
        elif op == "mult":
            r = a * b
            return {"operation": op, "result": r}
        elif op == "div":
            r = a / b
            return {"operation": op, "result": r}
        else:
            return {"operation failed due to":"invalid oparator"}
    except Exception as e:
        return {"Error":e}

@app.get("/status")
def status():
    return {"time":datetime.now(), "server":"MyServer on port: 8008"}


if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port=8008)