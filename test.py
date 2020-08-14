import requests


BASE = "http://127.0.0.1:5000/"

data = [{"likes": 10, "name": "Magnus", "views": 100},
        {"likes": 50, "name": "how to make restful API", "views": 500},
        {"likes": 100, "name": "cats", "views": 1000}]


for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())


response = requests.get(BASE + "video/0")
print(response.json())

response = requests.patch(BASE + "video/0", {"likes": 50, "name": "Magnus1", "views": 250})
print(response.json())

response = requests.get(BASE + "video/0")
print(response.json())

response = requests.delete(BASE + "video/0")
print(response)

response = requests.get(BASE + "video/0")
print(response.json())
