from flask import Flask, request, jsonify, render_template
from sklearn.externals import joblib

# Loading in the classifer for the stroke models. 
classifier = joblib.load("stroke_predictor.model")


# Defining the Flask app
app = Flask(__name__)

# Define the index.html
@app.route("/")
def index():
    return render_template("index.html")

# Create API endpoint based on HTML form
# @app.route("/api/predict")
# def predict():
#     age = float(request.args.get("age")) or 0
#     avg_glucose_level = float(request.args.get("agl")) or 0
    
# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)