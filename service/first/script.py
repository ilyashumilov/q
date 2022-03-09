import requests

r = requests.get('http://127.0.0.1:8000/')
a=[]
for i in r.json():
    a.append(i['number'])
print(a)


