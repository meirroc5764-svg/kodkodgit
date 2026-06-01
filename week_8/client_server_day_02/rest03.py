import requests

resters = requests.get("https://jsonplaceholder.typicode.com/posts")

my_dict = resters.json()

print(my_dict)

resters1 = requests.get("https://jsonplaceholder.typicode.com/users")

my_users_dict = resters1.json()

print(my_users_dict)

for dict in my_dict:
    print(dict["title"],my_users_dict[dict["userId"]-1]["name"])

