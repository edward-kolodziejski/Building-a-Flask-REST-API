import requests

BASE = "http://127.0.0.1:5000/"

# response  = requests.put(BASE + "video/1", {"likes":10, "name":"Tim", "views":1000000}) #{} getting extra data not visible in url
# print(response.json())
# input()
response  = requests.get(BASE + "video/6")
print(response.json())

