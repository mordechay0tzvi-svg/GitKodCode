import requests


BASE = "http://localhost:5686"

def add_name():
    name = input("enter name")
    id = input("enter id")
    r = requests.put(f"{BASE}/names/register", json={"name":name, "id":id})
    print(r.json())

def delete_name():
    identity = input("enter identification")
    r = requests.delete(f"{BASE}/names/{identity}")
    print(r.json())

def show_names():
    r = requests.get(f"{BASE}/names")
    print(r.json())

def get_name():
    identity = input("enter idetificatio")
    r = requests.get(f"{BASE}/names/{identity}")
    print(r.json())

def  main():
    add_name()
    add_name()
    show_names()
    get_name()
    delete_name()
    get_name()
    show_names()

if __name__ == "__main__":
    main()


