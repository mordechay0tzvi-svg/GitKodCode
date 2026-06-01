import requests
def students():
    r = requests.get("http://localhost:8008/students")
    print(r.json())

def top():
    r = requests.get("http://localhost:8008/students/top")
    print(r.json())

def average():
    r = requests.get("http://localhost:8008/students/average")
    print(r.json())

def count():
    r = requests.get("http://localhost:8008/students/count")
    print(r.json())

def student_id(student_id):
    r = requests.get(f"http://localhost:8008/students/{student_id}")
    print(r.json())

def main():
    students()
    student_id(2)
    top()
    average()
    count()


if __name__ == "__main__":
    main()



