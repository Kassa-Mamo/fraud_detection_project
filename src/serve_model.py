from flask import Flask, request, jsonify
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load model
model = joblib.load('models/fraud_detection_model.pkl')
scaler = StandardScaler()

@app.route('/predict', methods=['POST'])
def predict():
    """ Endpoint for making predictions """
    data = request.get_json()  # Get input from request (JSON)
    input_data = pd.DataFrame(data)  # Convert to DataFrame
    scaled_data = scaler.fit_transform(input_data)  # Scale data
    prediction = model.predict(scaled_data)  # Predict with the trained model
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
