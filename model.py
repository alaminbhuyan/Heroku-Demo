# load necessary module
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# load datasets
df = pd.read_excel('dataset.xlsx')
print(df.head())

# check null value
print(df.isnull().sum())

# handling null value
df.experience = df.experience.fillna(df.experience.median())
print(df.isnull().sum())

# split the feature and level
X = df.iloc[:,-1]
y = df.risk

print("features: ",X)
print()
print(y)

# Create the the model
model = LinearRegression()
model.fit(df[['speed','car_age','experience']],df.risk)

# predict value
print(model.predict([[170,10,3]]))

# saving the model
pickle.dump(model,open('regMode.pkl','wb'))

# load the model for check
my_model = pickle.load(open('regMode.pkl','rb'))
print("Predict: ",my_model.predict([[170,10,3]]))
import openpyxl