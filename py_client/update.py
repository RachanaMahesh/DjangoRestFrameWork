import requests

endpoint = "http://localhost:8000/api/products/8/update"

data = {"title":"Steel Water Bottle" , "price": 200 }
get_response = requests.put(endpoint, json= data)
print(get_response.json())