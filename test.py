import requests

BASE = "http://127.0.0.1:5000/"

data= [{"likes":10, "name":"How it is made?", "views":1000000},
        {"likes":240, "name":"Tim", "views":700000},
        {"likes":65, "name":"Tim", "views":900}]

for i in range(len(data)):
    response  = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)

input()
response  = requests.get(BASE + "video/2")
print(response.json())

