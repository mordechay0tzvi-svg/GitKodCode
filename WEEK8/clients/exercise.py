import requests
import fastapi
import uvicorn

# """Level 1 — Basic"""

# """Exercise 1"""

# r = requests.get("https://jsonplaceholder.typicode.com/users/1").json()
# print(r["name"])
# print(r["email"])
# print(r["address"]["city"])


# posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()
# print(len(posts))

# posts_id2 = requests.get("https://jsonplaceholder.typicode.com/posts?userId=2").json()
# for post in posts_id2:
#     print(post["title"])



# """Exercise 2"""

# def  safe_get(url):
#     r = requests.get(url)
#     if r.json()['status'] == 200:
#         return r.json()
#     elif  r.json()['status'] == 404:
#         return None
#     else:
#         raise Exception(f"Error code: {r.json()['status']}")

# """Exercise 3"""
# app = fastapi.FastAPI()
# @app.get("/greet")
# def greet(name="world"):
#     return  {"message": f"Hello, {name}!"}

# uvicorn.run(app, host = "0.0.0.0", port=8009)

# print(requests.get("http://localhost:8009/greet?name=Moshe").json()["message"])


"""Level 2 — Intermediate"""

"""Exercise 4 """

posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()
users = requests.get("https://jsonplaceholder.typicode.com/users").json()
articles = []
for post in posts:
    user_id = post["userId"]
    author = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}").json()["name"]
    articles.append(f'"{post["title"]}" by {author}')

for article in articles:
    print(article)