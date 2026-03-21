import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import pickle

data = pd.read_csv("cleaned_data.csv")  

TARGET_COLUMN = 'Sales'  
X = data.drop(TARGET_COLUMN, axis=1)
y = data[TARGET_COLUMN]

categorical_cols = X.select_dtypes(include=['object']).columns
label_encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le  

model = LinearRegression()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump({'model': model, 'encoders': label_encoders, 'columns': X.columns.tolist()}, f)

print("✅ Model and encoders saved successfully as model.pkl")