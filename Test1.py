import requests

url = "https://www.w3schools.com/python/python_conditions.asp"
response = requests.get(url)

print(response.text)