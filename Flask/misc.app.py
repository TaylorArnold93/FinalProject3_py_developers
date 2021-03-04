#     hypertension_mapper = {
#         0: [1, 0],
#         1: [0, 1]
#     }
#     hypertension = request.args.get("hypertension") or 0
#     if hypertension:
#         hypertension = 1
#     else:
#         hypertension = 0
    
#     heart_disease_mapper = {
#         0: [1, 0],
#         1: [0, 1]
#     }
#     heart_disease = request.args.get("heart_disease") or 0
#     if heart_disease:
#         heart_disease = 1
#     else:
#         heart_disease = 0

#     ever_married_mapper = {
#         0: [1, 0],
#         1: [0, 1]
#     }
#     ever_married = request.args.get("ever_married") or 0
#     if ever_married:
#         ever_married = 1
#     else:
#         ever_married = 0

#     # Create a list of the user's given features
#     # We one-hot-encoded the categorical columns,
#     # so we must use a mapper to pass the user's single input
#     # to each relevant column

#     # In our initial data analysis we noticed that,
#     # the smoking_status data does not reflect statements made in a scientific journal
#     # on the effects of smoking on having a stroke
#     # We therefore opted not to use smoking_status as a feature
#     # We leave it commented it out here,
#     # so that we may return at a later time if we decide to use this in some way
#     features = [[age,
#                  average_glucose_level,
#                 #  bmi,
#                  work_type_mapper[work_type][0],
#                  work_type_mapper[work_type][1],
#                  work_type_mapper[work_type][2],
#                  smoking_status_mapper[smoking_status][0],
#                  smoking_status_mapper[smoking_status][1],
#                  smoking_status_mapper[smoking_status][2],
#                  hypertension_mapper[hypertension][0],
#                  hypertension_mapper[hypertension][1],
#                  heart_disease_mapper[heart_disease][0],
#                  heart_disease_mapper[heart_disease][1],
#                  ever_married_mapper[ever_married][0],
#                  ever_married_mapper[ever_married][1]]]

#     # Scale features
#     scaled_features = standard_scaler.transform(features)

#     # Make a prediction based on the user's input
#     prediction = classifier.predict(scaled_features)
#     # Determine prediction probability
#     prediction_probability = classifier.predict_proba(scaled_features)

#     # print(100*"#")
#     # print(features)
#     # print(100*"#")

#     # Return a JSON giving the prediction and probability thereof
#     return jsonify({"stroke_prediction": prediction.tolist(),
#                     "stroke_prediction_probability": prediction_probability.tolist(),
#                     "features": features})
