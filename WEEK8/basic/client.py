import requests
def test_basic_ping():
    r = requests.get("http://localhost:8008/ping")
    print(r.json())

def test_basic_greet_name(name):
    r = requests.get(f"http://localhost:8008/greet/{name}")
    print(r.json())


def main():
    test_basic_ping()
    test_basic_greet_name("test")


if __name__ == "__main__":
    main()

