# pip install Flask

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.preprocessing import StandardScaler

# Loading in the classifer for the stroke models. 
classifier = joblib.load("stroke_predictor.model")


# Defining the Flask app
app = Flask(__name__)

# Loading the Pickle 
model = pickle.load(open('model.pkl', 'rb'))

# Define the index.html
@app.route('/')
def home():
    return render_template('index.html')

# Create API endpoint based on HTML form
@app.route("/api/predict")
 def predict():
#     age = float(request.args.get("age")) or 0
#     avg_glucose_level = float(request.args.get("agl")) or 0

    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    final_features = scaler.transform(final_features)    
    prediction = model.predict(final_features)
    print("final features",final_features)
    print("prediction:",prediction)
    output = round(prediction[0], 2)
    print(output)

    if output == 0:
        return render_template('index.html', prediction_text='THE PATIENT IS NOT LIKELY TO HAVE A HEART FAILURE')
    else:
         return render_template('index.html', prediction_text='THE PATIENT IS LIKELY TO HAVE A HEART FAILURE')
        
@app.route('/predict_api',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


function 

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)