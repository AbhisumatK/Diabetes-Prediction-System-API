from pydantic import BaseModel
#
class diab(BaseModel):
    gender: float 
    age: float 
    hypertension: float 
    heart_disease: float
    smoking_history: float
    bmi: float
    HbA1c_level: float
    blood_glucose_level: float
