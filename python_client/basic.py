import requests

# endpoint_1 = "https://httpbin.org/anything&quot;
# endpoint_2 = "http://127.0.0.1:8000&quot;
endpoint_3 = "http://127.0.0.1:8000/api/"
# endpoint_3 = "http://127.0.0.1:8000/api/?query=justtestingit&quot;


# get_response = requests.get(endpoint_1, json={"query": "the legend...!"})
# get_response = requests.get(endpoint_2)
# get_response = requests.get(endpoint_3)
# get_response = requests.get(endpoint_3, params={"product_id": 123}, json={'query': 'hello world'})
# get_response = requests.get(endpoint_3, json={'query': 'hello world'})

get_response = requests.post(endpoint_3, json={"title": "Title004", "content": "Content004", "price": 300})

# print(get_response.text)
print(get_response.json())

print(get_response.status_code)
