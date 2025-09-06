from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import pandas as pd
import joblib
import os

# Create Flask app
app = Flask(__name__)
CORS(app)

# Load the trained model and feature columns
model_path = os.path.join('models', 'water_prediction_model.pkl')
feature_columns_path = os.path.join('models', 'feature_columns.pkl')

try:
    model = joblib.load(model_path)
    feature_columns = joblib.load(feature_columns_path)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None
    feature_columns = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

@app.route('/awareness')
def awareness():
    return render_template('awareness.html')

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or feature_columns is None:
        return jsonify({'error': 'Model not loaded properly'}), 500
    
    try:
        # Get the input data from the frontend
        data = request.get_json()

        # Convert input JSON to DataFrame
        input_data = pd.DataFrame([data])

        # Map crop names to standardized categories (used during training)
        crop_mapping = {
            "wheat": "crop_type_Wheat",
            "rice": "crop_type_Rice",
            "soybean": "crop_type_Soybean",
            "maize": "crop_type_Maize"
        }

        # Add one-hot encoded crop columns
        for crop in crop_mapping.values():
            input_data[crop] = 0  # Initialize all crops with 0

        # Set the correct crop column to 1
        if data.get("crop_type") in crop_mapping:
            input_data[crop_mapping[data["crop_type"]]] = 1
        else:
            return jsonify({'error': 'Invalid crop type provided.'}), 400

        # Drop the raw 'crop_type' column as it is no longer needed
        input_data.drop(columns=['crop_type'], inplace=True)

        # Ensure input data matches the feature columns used during training
        input_data = input_data.reindex(columns=feature_columns, fill_value=0)

        # Make the prediction
        predicted_water = model.predict(input_data)

        # Return the prediction result
        return jsonify({'predicted_water_usage': predicted_water[0]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Serve static files
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
