import requests

# endpoint = "https://httpbin.org/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000"


response = requests.get(endpoint)
print(response.status_code)