import requests

endpoint = "http://localhost:8000/api/products/"
data = {"title": "Glass Container", "price": 400}
get_response = requests.post(endpoint,json= data)
print(get_response.json())