import json


from user import User

with open("my_file.txt", 'r') as f:
    json_data = json.load(f)
    user = User.from_json(json_data)
print(user)
print(user.movies)