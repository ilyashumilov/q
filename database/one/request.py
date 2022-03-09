import requests

r = requests.get('http://127.0.0.1:8000/')
print(r.json())
for i in r.json():
    print(i['number'])