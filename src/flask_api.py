 import requests
import json

url = 'http://127.0.0.1:5000/predict'
data = {
    'feature1': 20,
    'feature2': 15,
    # Add other features here
}

response = requests.post(url, json=data)
print(response.json())

