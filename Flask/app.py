# pip install Flask

import numpy as np
from flask import Flask, request, jsonify, render_template,  url_for, flash, redirect

# Defining the Flask app
app = Flask(__name__)

@app.route('/learn-more', methods=['GET'])
def lessons():
    return render_template('Lessons.html')


# Define the index.html
@app.route('/', methods=['GET', 'POST'])
def home():
    output = 0
    if request.method == "POST":
        age = float(request.form.get("age")) or 0
        work_type = request.form.get("work_type")
        smoking_status = request.form.get("smoking_status")
        avg_glucose_level = float(request.form.get("avg_glucose_level", 0)) or 0
        hypertension = request.form.get("hypertension")
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
        if hypertension == "on":
            output += 0.75
        else: 
            output += 0.0
        if output < 0.50:
            prediction_text = 'The patient is NOT likely to have a Stroke'
        else:
            prediction_text = 'The patient is LIKELY to have a Stroke'
        return render_template('index.html', prediction_text=prediction_text)
    else:
         return render_template('index.html')

        
"""@app.route('/',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)
"""

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)