import requests

# django localhost:8000/api/
endpoint = "http://127.0.0.1:8000/api/products/create/"

# HTTP request
data = {
    "title": "Title010",
    "price": 35
}
get_response = requests.post(endpoint, json=data)

# gives the response in python dictionary format
print(get_response.json())

# gives the status code
print(get_response.status_code)