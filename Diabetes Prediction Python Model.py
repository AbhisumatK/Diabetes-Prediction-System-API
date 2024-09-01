import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
#from sklearn.metrics import accuracy_score

data = pd.read_csv('diabetes_prediction_dataset.csv')

df_no_diabetes = data[data['diabetes'] == 0]
df_diabetes = data[data['diabetes'] == 1]

df_no_diabetes_sampled = df_no_diabetes.sample(n=8500, random_state=42)
df_balanced = pd.concat([df_no_diabetes_sampled, df_diabetes])
data = df_balanced.sample(frac=1, random_state=42).reset_index(drop=True)

data['gender'] = data['gender'].map({'Male': 1, 'Female': 0})

data['smoking_history'] = data['smoking_history'].map({
    'former': 1,
    'not current': 1,
    'current': 2,
    'never': 0,
    'ever': 0,
    'No Info': -1
})

data = data.dropna()

x = data.drop(columns='diabetes', axis=1)
y = data['diabetes']

scaler = StandardScaler()
scaler.fit(x)
standardized_data = scaler.transform(x)
x = standardized_data

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y, random_state=2)
classifier = svm.SVC(kernel='linear')
classifier.fit(x_train, y_train)

gend = str(input('Enter your gender (m/f): '))
if gend=='m':
    gend = 1
elif gend=='f':
    gend = 0
else:
    print('Invalid Input')

age = eval(input('Enter your age: '))

ht = str(input('Do you have hypertension? (y/n): '))
if ht=='y':
    ht = 1
elif ht=='n':
    ht = 0
else:
    print('Invalid Input')

hd = str(input('Do you suffer from any form of heart disease? (y/n): '))
if hd=='y':
    hd = 1
elif hd=='n':
    hd = 0
else:
    print('Invalid Input')

sh = str(input('What is your smoking history? (never smoked/former smoker/current smoker/do not wish to disclose): '))
if (sh=='never smoked'):
    sh = 0
elif (sh=='former smoker'):
    sh = 1
elif(sh=='current smoker'):
    sh = 2
elif(sh=='do not wish to disclose'):
    sh = -1
else:
    print('Invalid Input')

bmi = eval(input('Enter your bmi: '))

hg_level = eval(input('Enter your haemoglobin level: '))

bgl = eval(input('Enter your blood glucose level: '))

input = [gend,age,ht,hd,sh,bmi,hg_level,bgl]
input_data_as_np_array = np.asarray(input)

input_data_reshaped = input_data_as_np_array.reshape(1,-1)

#standardizing the input data
std_data = scaler.transform(input_data_reshaped)

prediction = classifier.predict(std_data)

if (prediction[0] == 0):
    print('The person is NOT diabetic')
else:
    print('The person is diabetic')