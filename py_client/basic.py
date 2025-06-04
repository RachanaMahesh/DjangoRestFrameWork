import requests

endpoint = "http://localhost:8000/" 
get_response = requests.post(endpoint, json={"title": "Abc123", "content": "Hello world", "price": "abc134"}) # HTTP Request
print(get_response.headers)
print(get_response.text) # print raw text response
print(get_response.status_code)



# HTTP Request -> Non - APIrequest -> HTML # will return an HTML document
# for http request u will get a html that's made for the browser that's made for humans to look at
# endpoint = "https://github.com/" # http request # will return an HTML document
# get_response = requests.get(endpoint)
# print(get_response.text) # print the source code

# request : is basically an API -> get() is a method built into it . Using this library is a form of using an API
# Example for API: phone -> camera -> App -> API -> CAMERA
# request.get() is an example of library API and not REST API

# REST APIs wt we r using & wt we r building they have to do with API
# REST API --> Web based API - doesn't mean that it has to go across internet but it dos mean that it's going to use something called an http request

# REST API HTTP Request -> JSON / XML  :  
# web API will allow ur application to interact with another application through web(some sort of internet request)
# REST APIs aren't meant for humans to look at instead meant for software to communicate with each other over the web
# JavaScript Object Nototion ~ Python Dict
# endpoint = "https://httpbin.org/"
# endpoint = "https://httpbin.org/anything" 
# get_response = requests.get(endpoint)
# # print(get_response.text) # returns JSON data
# # print(get_response.json()) # return a python dictinary

# print("------------------------------------------------------------------------------------")

# using request lib we can pass our own json data 
# endpoint = "http://localhost:8000/api"get_response = requests.get(endpoint, json={"query":"Hello World"})
# print(get_response.text) # O/P: "data": "{\"query\": \"Hello World\"}", "Content-Type": "application/json",

# get_response = requests.get(endpoint, data={"query":"Hello World"})
# print(get_response.text) # O/P: "form": {"query": "Hello World"} , "Content-Type": "application/x-www-form-urlencoded",
# print(get_response.status_code)

# print("------------------------------------------------------------------------------------")

# endpoint = "http://localhost:8000/api/"
# get_response = requests.post(endpoint, json={"title": "Product_11" , "content": "Product_11", "price": 123})
# get_response = requests.get(endpoint , params={"abc":123},json={"query": "Hello World!"})
# print(get_response.headers)
# print(get_response.status_code)
# print(get_response)
# print(get_response.json())

# endpoint = "http://localhost:8000/" #http://127.0.0.1:8000/ 
# get_response = requests.post(endpoint, json={"title": "Abc123", "content": "Hello world", "price": "abc134"}) # HTTP Request
# print(get_response.headers)
# print(get_response.text) # print raw text response
# print(get_response.status_code)



# 1. 1st half : creating a way to consume an API
# 2. 2nd half : creating a way that we can actually design the API  we can actually just dictate what should be consumed or what can be consumed

