import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

data = pd.read_csv("cleaned_data.csv")
data.columns = data.columns.str.strip()

drop_cols = [
    'Order ID', 'Product ID', 'Customer ID', 'Product Name', 'Row ID',
    'Order Date', 'Ship Date', 'City', 'State/Province', 'Postal Code', 'Country/Region'
]
for col in drop_cols:
    if col in data.columns:
        data.drop(col, axis=1, inplace=True)

categorical_cols = [c for c in ['Factory', 'Region', 'Ship Mode', 'Division'] if c in data.columns]
data = pd.get_dummies(data, columns=categorical_cols)


X = data.drop('Lead Time', axis=1)
y = data['Lead Time']

model = RandomForestRegressor(n_estimators=50, max_depth=10, random_state=42)
model.fit(X, y)

joblib.dump(model, 'model.pkl', compress=3)  
joblib.dump(X.columns, 'columns.pkl')

print("Model trained")