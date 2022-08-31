import requests

# endpoint = "https://httpbin.org/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api"


response = requests.get(endpoint, json={"product_id": 123})
print(response.json())