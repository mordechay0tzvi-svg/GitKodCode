import requests
def test_initial_get():
    r = requests.get("http://localhost:8008/")
    print(r.json())

def test_user_id(user_id):
    r = requests.get(f"http://localhost:8008/users/{user_id}")
    print(r.json())

def test_users_admin():
    r = requests.get("http://localhost:8008/users/admin")
    print(r.json())

def test_calc_op():
    r = requests.get("http://localhost:8008/calc/8/div/2")
    print(r.json())

def main():
    test_initial_get()
    test_user_id("test_id")
    test_users_admin()
    test_calc_op()


if __name__ == "__main__":
    main()

