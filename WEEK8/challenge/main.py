from fastapi import FastAPI
import uvicorn

app = FastAPI()
grades = {
"1": {"name": "Moshe", "grade": 88},
"2": {"name": "Yaakov", "grade": 75},
"3": {"name": "David", "grade": 92},
}

@app.get("/students")
def students():
    return grades

@app.get("/students/top")
def top():
    return {"max score":(max(grades.values(), key=lambda x: x["grade"])["name"])}

@app.get("/students/average")
def average():
    return {"average":sum(student["grade"] for student in grades.values()) / len(grades)}

@app.get("/students/count")
def count():
    return {"number of students":len(grades)}

@app.get("/students/{student_id}")
def student(student_id):
    return {f"student:{student_id}": grades[student_id]}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port = 8008)
