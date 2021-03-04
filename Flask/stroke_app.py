# pip install Flask

import numpy as np
from flask import Flask, request, jsonify, render_template
from sklearn.preprocessing import StandardScaler

# Loading in the classifer for the stroke models. 
# classifier = joblib.load("stroke_predictor.model")

# Defining the Flask app
app = Flask(__name__)

# Define the index.html
@app.route('/')
def home():
    return render_template('index.html')

# Create API endpoint based on HTML form
@app.route("/api/predict")

def predict():
    age = float(request.args.get("age")) or 0
    avg_glucose_level = float(request.args.get("agl")) or 0
    bmi = float(request.args.get("bmi")) or 0

    work_type_mapper = {
        "self_employed": [1,0,0,0,0],
        "children": [0,1,0,0,0],
        "Govt_job": [0,0,1,0,0],
        "private" : [0,0,0,1,0],
        "never_worked": [0,0,0,0,1]      
     }

    work_type = request.args.get("work_type")

    smoking_status_mapper = {
        "formerly_smoked": [0, 0, 1, 0],
        "never_smoked": [0, 1, 0, 0],
        "smokes": [1, 0, 0, 0],
        "Unknown": [0, 0, 0, 1]
    }
    
    smoking_status = request.args.get("smoking_status")

    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    final_features = scaler.transform(final_features)    
    prediction = model.predict(final_features)
    print("final features",final_features)
    print("prediction:",prediction)
    output = round(prediction[0], 2)
    print(output)

    if output == 0:
        return render_template('index.html', prediction_text='The Patient is NOT likely to have a Stroke')
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