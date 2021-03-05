# pip install Flask

import numpy as np
from flask import Flask, request, jsonify, render_template,  url_for, flash, redirect
from sklearn.preprocessing import StandardScaler

# Loading in the classifer for the stroke models. 
# classifier = joblib.load("stroke_predictor.model")

# Defining the Flask app
app = Flask(__name__)

# Define the index.html
@app.route('/')
def home():
    print(request)
    output = 0
    if request.args: 
        age = float(request.args.get("age")) or 0
        work_type = request.args.get("work_type")
        smoking_status = request.args.get("smoking_status")
        avg_glucose_level = float(request.args.get("agl")) or 0
        if int(age) > 60: 
            output += 0.25
        if smoking_status == "smokes":
            output += 0.50

    if output < 0.50:
        return render_template('index.html', prediction_text='The patient is NOT likely to have a Stroke')
    else:
         return render_template('index.html', prediction_text='The patient is LIKELY to have a Stroke')
        
@app.route('/predict_api',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)