import requests

x = requests.get('http://127.0.0.1:8000/demo-app-name/?name=john')

print(x.text)
