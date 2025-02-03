import requests

url = "https://jsonplaceholder.typicode.com/posts/1"  # Sample API
response = requests.get(url)

if response.status_code == 200:
    print("Response JSON:", response.json())
else:
    print("Failed to fetch data. Status code:", response.status_code)
