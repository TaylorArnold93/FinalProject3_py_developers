import pandas as pd 
import warnings 
warnings.filterwarnings('ignore')

### change path
data = pd.read_csv('Data/processed_data.csv')

# select X and y values
X = data[['Age', 'Hypertension', 'Heart Disease', 'Avg Glucose Level', 'BMI', 'Smoking Status_formerly smoked', 'Smoking Status_smokes']]
y = data['Stroke'].values.reshape(-1,1)

# train test split data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)


# StandardScaler
from sklearn.preprocessing import StandardScaler

X_scaler = StandardScaler().fit(X_train)
y_scaler = StandardScaler().fit(y_train)

X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)
y_train_scaled = y_scaler.transform(y_train)
y_test_scaled = y_scaler.transform(y_test)

# create classifier
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()

# fit train data
classifier.fit(X_train, y_train)

# score our classifier
train_score = classifier.score(X_train, y_train)
test_score = classifier.score(X_test, y_test)

print(f'Train model score: {train_score}') # this should be over 0.90 to be a good model
print(f'Test model score: {test_score}') # this should be over 0.90 to be a good model

# make prediction with user input (input from HTML)
# ---------------------------------------------------------------------------------
# age: 100,
# hypertension: 1
# heartdisease: 1
# avgglucose: 500
# BMI: 35
# Smoking Status_formerly smoked: 1
# Smoking Status_smokes: 1

random_person = [[100, 1, 1, 300, 35, 1, 1]] # this will be the user input from the html

# 1 likely
# 0 not likely

prediction = classifier.predict(random_person)

if prediction == 1:
    print('You are at risk of having a stroke')
else:
    print('You are not at risk of having a stroke')