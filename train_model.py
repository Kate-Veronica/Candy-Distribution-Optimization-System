import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("cleaned_data.csv")

target = "Sales"
X = data.drop(columns=[target])
y = data[target]

categorical_cols = X.select_dtypes(include=['object']).columns

encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col].astype(str))
    encoders[col] = le

model = LinearRegression()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

columns = X.columns.tolist()
with open("columns.pkl", "wb") as f:
    pickle.dump(columns, f)

with open("encoders.pkl", "wb") as f:
    pickle.dump(encoders, f)

print("✅ Model, columns, and encoders saved successfully!")