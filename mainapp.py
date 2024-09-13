# 1. Library imports
import uvicorn
from fastapi import FastAPI
from diabetes import diab
import pickle
import os
from dotenv import load_dotenv
load_dotenv()
# 2. Create the app object
app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)
PORT = os.getenv('PORT') or 3000

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To my API': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_diabetes(data:diab):
    data = data.dict()
    gender=data['gender']
    age=data['age']
    hypertension=data['hypertension']
    heart_disease=data['heart_disease']
    smoking_history=data['smoking_history']
    bmi=data['bmi']
    HbA1c_level=data['HbA1c_level']
    blood_glucose_level=data['blood_glucose_level']

    prediction = classifier.predict([[gender,age,hypertension,heart_disease,smoking_history,bmi,HbA1c_level,blood_glucose_level]])
    if (prediction == 0):
        prediction = 'The person is NOT diabetic'
    else:
        prediction = 'The person is diabetic'
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(mainapp, host = '0.0.0.0', PORT)
    
#uvicorn app:app --reload
