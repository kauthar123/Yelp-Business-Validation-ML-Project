from flask import Flask, request, jsonify  # Import necessary modules from Flask
import pickle  # Import pickle for loading the model
import numpy as np  # Import NumPy for numerical operations

# Load your trained model (assuming it's a scikit-learn model)
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)  # Load the model from a file

app = Flask(__name__)  # Create a Flask application instance

@app.route('/predict', methods=['POST'])  # Define the '/predict' route with POST method
def predict():
    data = request.json  # Get JSON data from the request
    features = np.array(data['features']).reshape(1, -1)  # Convert features to a NumPy array and reshape
    prediction = model.predict(features)  # Use the model to make a prediction
    return jsonify({'prediction': prediction[0]})  # Return the prediction as JSON

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode