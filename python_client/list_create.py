import requests
from getpass import getpass
from django.http import HttpResponse

# entering the username and password through command prompt
# -------------------------------------------------------------------------------------------------

# authentication endpoint
auth_endpoint = "http://127.0.0.1:8000/api/auth/"

# username and password
username = input("Enter your username: ")
password = getpass("Enter your password: ")

auth_response = requests.post(auth_endpoint, json={'username':username, 'password':password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        'Authorization': 'Token {}'.format(token)
    }

    # django localhost:8000/api/
    endpoint = "http://127.0.0.1:8000/api/products/list/create/"

    # HTTP request: GET
    get_response = requests.get(endpoint, headers=headers)

    # data = {
    #     "title": "Title013",
    #     "price": 170
    # }

    # HTTP request: POST
    # get_response = requests.post(endpoint, json=data)

    # gives the response in python dictionary format
    print(get_response.json())

    # gives the status code
    print(get_response.status_code)


# testing by putting the token directly from the admin panel after running the above authentication
# -------------------------------------------------------------------------------------------------

# headers = {
#     'Authorization': 'Token dd2bceb5627a1aaa22c02599572f43b95dee16c3'
# }

# # django localhost:8000/api/
# endpoint = "http://127.0.0.1:8000/api/products/list/create/&quot;

# # HTTP request: GET
# get_response = requests.get(endpoint, headers=headers)

# # data = {
# #     "title": "Title013",
# #     "price": 170
# # }

# # HTTP request: POST
# # get_response = requests.post(endpoint, json=data)

# # gives the response in python dictionary format
# print(get_response.json())

# # gives the status code
# print(get_response.status_code)