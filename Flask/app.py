# pip install Flask

import numpy as np
from flask import Flask, request, jsonify, render_template,  url_for, flash, redirect
from sklearn.preprocessing import StandardScaler

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
        avg_glucose_level = float(request.args.get("avg_glucose_level")) or 0
        hypertension = request.args.get("hypertension")
        if int(age) > 60: 
            output += 0.25
        if smoking_status == "smokes":
            output += 0.75
        elif smoking_status == "formerly_smoked":
            output += 0.50
        elif smoking_status == "never smoked":
            output += 0.0
        elif smoking_status == "Unknown":
            output += 0.25
        if work_type == "Self_employed":
            output += 0.75
        elif work_type == "Private":
            output += 0.50
        elif work_type == "Govt_job":
            output += 0.25
        elif work_type == "Never_worked":
            output += 0.0
        if int(avg_glucose_level) > 100:
            output += 0.50
        print(hypertension)
        if hypertension == "on":
            output += 0.75
        else: 
            output += 0.0

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