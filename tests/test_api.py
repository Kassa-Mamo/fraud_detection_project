 
import pytest
import requests

def test_predict_api():
    url = 'http://127.0.0.1:5000/predict'
    data = {
        'feature1': 20,
        'feature2': 15,
        # Add other features here
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert 'prediction' in response.json()
