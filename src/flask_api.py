import requests
import json

# Define the URL of the Flask API
url = 'http://127.0.0.1:5000/predict'

# Define the input data as a dictionary. Replace the values with actual feature values.
data = {
    'feature1': 20,
    'feature2': 15,
    # Add other features here
}

# Function to make a POST request to the Flask API and handle the response
def make_prediction(data):
    try:
        # Sending the POST request with the input data as JSON
        response = requests.post(url, json=data)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            prediction = response.json()  # Parse the JSON response from the API
            return prediction
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        # Handle any exception that occurs during the request (e.g., network issues)
        print(f"Error while making the request: {e}")
        return None

# Main block to execute the function and print the prediction
if __name__ == "__main__":
    prediction = make_prediction(data)
    if prediction:
        print("Prediction Response:", prediction)
    else:
        print("Failed to get a prediction.")
