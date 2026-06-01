import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
print(response.json())
print(response.text)
data = response.json()
print(data["title"])
print(data["userId"])




new_post = {"title": "My First Post","body": "This is the content","userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts",json=new_post)
print(response.status_code)
print(response.json())





updated = {"id": 1, "title": "New Title", "body": "New content", "userId":1}
r = requests.put("https://jsonplaceholder.typicode.com/posts/1",json=updated)
print(r.status_code)
r = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(r.status_code)





params = {"userId": 1}
response = requests.get("https://jsonplaceholder.typicode.com/posts",params=params )
posts = response.json()
print(f"Found {len(posts)} posts for user 1")
for post in posts[:3]:
    print(f" - {post['title']}")





