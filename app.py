from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Read values from form
    bedrooms = float(request.form['bedrooms'])
    bathrooms = float(request.form['bathrooms'])
    sqft_living = float(request.form['sqft_living'])
    year = float(request.form['year'])
    month = float(request.form['month'])
    day = float(request.form['day'])
    country = float(request.form['country'])

    # Simple linear formula (example weights)
    price = (
        bedrooms * 50000 +
        bathrooms * 30000 +
        sqft_living * 200 +
        year * 100 +
        month * 500 +
        day * 100 +
        country * 10000
    )

    return render_template('index.html', result=f"Predicted House Price: ₹ {round(price, 2)}")

if __name__ == "__main__":
    app.run(debug=True)