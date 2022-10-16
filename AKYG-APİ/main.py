import requests

URL = "https://api.thecatapi.com/v1/images/search"
result = requests.get(URL)
data = result.json()
print(data)
