# import requests
# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# print(response.status_code)
# print(response.json())
# print(response.text)
# data = response.json()
# print(data["title"])
# print(data["userId"])




# new_post = {"title": "My First Post","body": "This is the content","userId": 1}
# response = requests.post("https://jsonplaceholder.typicode.com/posts",json=new_post)
# print(response.status_code)
# print(response.json())





# updated = {"id": 1, "title": "New Title", "body": "New content", "userId":1}
# r = requests.put("https://jsonplaceholder.typicode.com/posts/1",json=updated)
# print(r.status_code)
# r = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
# print(r.status_code)





# params = {"userId": 1}
# response = requests.get("https://jsonplaceholder.typicode.com/posts",params=params )
# posts = response.json()
# print(f"Found {len(posts)} posts for user 1")
# for post in posts[:3]:
#     print(f" - {post['title']}")



from fastapi import FastAPI

app = FastAPI()
@app.get("/users")
def get_users(role: str = "all", page: int = 1):
    return {"role": role, "page": page, "users": []}

@app.get("/users/{user_id}") 
def get_user(user_id: int):
    return {"user_id": user_id}

import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts/99999")
if response.status_code == 200:
    print("Got data:", response.json())
elif response.status_code == 404:
    print("Not found")
else:
    print(f"Unexpected status: {response.status_code}")



