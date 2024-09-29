import streamlit as st  # Import Streamlit for building the web app
import requests  # Import requests for making HTTP requests
import numpy as np  # Import NumPy for numerical operations

# URL of your Flask API
FLASK_API_URL = 'http://localhost:5000/predict'  # Specify the API endpoint

st.title('Model Prediction App')  # Set the title of the Streamlit app

# Input fields for features
feature1 = st.number_input('Feature 1')  # Input for the first feature
feature2 = st.number_input('Feature 2')  # Input for the second feature
feature3 = st.number_input('Feature 3')  # Input for the third feature

if st.button('Predict'):  # When the "Predict" button is clicked
    features = np.array([feature1, feature2, feature3]).tolist()  # Collect features into a list
    response = requests.post(FLASK_API_URL, json={'features': features})  # Send a POST request to the Flask API
    
    if response.status_code == 200:  # Check if the request was successful
        prediction = response.json()['prediction']  # Extract the prediction from the response
        st.success(f'Predicted Value: {prediction}')  # Display the prediction to the user
    else:
        st.error('Error in prediction request')  # Display an error message if the request failed