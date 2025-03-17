import logging
from flask import Flask, request, jsonify
import numpy as np
import joblib
import os

app = Flask(__name__)

# Configure the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# File handler to save logs to a file
file_handler = logging.FileHandler('api.log')
file_handler.setLevel(logging.INFO)

# Formatter to define the log format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(file_handler)


# Get the absolute path of the model file
model_path = os.path.join(os.path.dirname(__file__), '../models/best_linear_model.pkl')

# Load the model with error handling
try:
    model = joblib.load(model_path)
    logger.info("Model loaded successfully.")
except Exception as e:
    logger.error(f"Error loading model: {e}")
    model = None

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Validate input fields
        required_fields = ['area', 'total_rooms', 'luxury_count', 'furnishingstatus_encoded']
        for field in required_fields:
            if field not in data:
                logger.error(f"Missing field: {field}")
                return jsonify({"error": f"Missing field: {field}"}), 400

        # Prepare features for prediction
        features = [
            data['area'],
            data['total_rooms'],
            data['luxury_count'],
            data['furnishingstatus_encoded']
        ]

        # Convert to 2D array
        features = np.array(features).reshape(1, -1)

        # Predict the price
        prediction = model.predict(features)
        output = prediction[0]
        logger.info(f"Prediction successful: {output}")

        return jsonify({"predicted_price": output})

    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return jsonify({"error": "An error occurred during prediction"}), 500

if __name__ == "__main__":
    app.run(debug=True)
