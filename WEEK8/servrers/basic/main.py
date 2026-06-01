from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/ping")
def ping():
    return {"status":"pong"}

@app.get("/greet/{name}")
def greet(name):
    return  {"message": f"Hello, {name}!"}



if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port=8008)


