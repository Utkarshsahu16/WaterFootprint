# Water Footprint Application

A Flask-based web application for water footprint analysis and prediction using machine learning.

## Features

- **Water Usage Prediction**: ML model to predict water usage based on environmental factors
- **Interactive Calculator**: Web interface for inputting data and getting predictions
- **Educational Content**: Information about water conservation and awareness
- **Analysis Tools**: Visual charts and analysis of water footprint data
- **Multi-language Support**: Google Translate integration

## Project Structure

```
water-footprint-app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── render.yaml           # Render deployment configuration
├── models/               # ML model files
│   ├── water_prediction_model.pkl
│   └── feature_columns.pkl
├── static/               # Static assets
│   ├── css/             # Stylesheets
│   ├── js/              # JavaScript files
│   ├── images/          # Images and logos
│   └── fonts/           # Font files
└── templates/           # HTML templates
    ├── index.html       # Home page
    ├── calculator.html  # Water prediction calculator
    ├── about.html       # About page
    ├── awareness.html   # Water awareness content
    ├── analysis.html    # Analysis and charts
    ├── faq.html         # Frequently asked questions
    └── education.html   # Educational content
```

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Locally

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Deployment on Render

1. Push your code to a Git repository (GitHub, GitLab, etc.)
2. Connect your repository to Render
3. Render will automatically detect the `render.yaml` configuration
4. The application will be deployed and available at the provided URL

## API Endpoints

- `GET /` - Home page
- `GET /calculator` - Water prediction calculator
- `GET /about` - About page
- `GET /awareness` - Water awareness content
- `GET /analysis` - Analysis and charts
- `GET /faq` - FAQ page
- `GET /education` - Educational content
- `POST /predict` - ML prediction endpoint

## ML Model

The application uses a Random Forest Regressor model trained on agricultural data to predict water usage based on:
- Temperature (°C)
- Humidity (%)
- Soil Moisture (%)
- Rainfall (mm)
- Crop Type (Wheat, Rice, Soybean, Maize)

## Technologies Used

- **Backend**: Flask, Python
- **Frontend**: HTML, CSS, JavaScript
- **ML**: scikit-learn, pandas, joblib
- **Charts**: AnyChart
- **Animations**: GSAP, Locomotive Scroll
- **Deployment**: Render, Gunicorn

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.
