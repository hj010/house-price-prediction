Introduction

This project predicts house prices based on various features using regression models. The pipeline includes data preprocessing, feature engineering, model training, optimization, and deployment as a REST API.



Data Preprocessing and Feature Engineering

Steps Taken:
Data Loading:
Loaded the dataset from a CSV file using Pandas.
Data Cleaning:
Checked for missing values (none found).
Performed basic data exploration to understand the structure and distribution.
Feature Engineering:
Created new features to enhance prediction accuracy:
total_rooms = bedrooms + bathrooms + stories + parking
luxury_count = Sum of binary luxury features (airconditioning, guestroom, hotwaterheating, prefarea)
Encoded the categorical feature furnishingstatus into furnishingstatus_encoded.
Feature Selection:
Reduced input features to four main features:
area, total_rooms, luxury_count, furnishingstatus_encoded



 Model Selection and Optimization

Trained Models:
Linear Regression
Random Forest Regressor
Evaluation Metrics:
Root Mean Squared Error (RMSE)
Mean Absolute Error (MAE)
R² Score
Results:
Model	            RMSE	      MAE	   R²
Linear Regression	1,345,743	960,709	0.64
Random Forest	1,425,033	1,007,792	0.60

Deployment Strategy

API Development:
Built a REST API using Flask to predict house prices.
The API accepts a JSON input and returns the predicted price.
API Endpoint:

POST http://<server_address>:5000/predict
Sample Request:

curl -X POST http://<server_address>:5000/predict \
    -H "Content-Type: application/json" \
    -d '{
        "area": 7420,
        "total_rooms": 11,
        "luxury_count": 2,
        "furnishingstatus_encoded": 2
    }'
Sample Response:

{
    "predicted_price": 9126120.09
}


 Logging and Error Handling

Implemented robust error handling for invalid inputs.
Used Python’s logging module to track API requests and errors.



Usage Instructions

Clone the repository:
git clone https://github.com/yourusername/house-price-prediction.git

Install dependencies:
pip install -r requirements.txt

Run the API:
python app.py

Test the API: Use the curl command or any API client like Postman.


Technologies Used

Python (Flask, Scikit-learn)
Pandas, NumPy
Matplotlib, Seaborn