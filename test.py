import requests

BASE = "http://127.0.0.1:5000/"

response  = requests.put(BASE + "video/1", {"likes":10}) #{} getting extra data not visible in url
print(response.json())

