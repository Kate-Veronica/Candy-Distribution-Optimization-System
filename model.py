<<<<<<< HEAD
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
=======
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import joblib

data = pd.read_csv("cleaned_data.csv")
data.columns = data.columns.str.strip()

drop_cols = ['Order ID', 'Product ID', 'Customer ID', 'Product Name', 'Row ID', 
             'Country/Region', 'City', 'State/Province', 'Postal Code', 'Division']
data = data.drop(columns=[c for c in drop_cols if c in data.columns])

date_cols = ['Order Date', 'Ship Date']
for col in date_cols:
    if col in data.columns:
        data[col] = pd.to_datetime(data[col]).map(pd.Timestamp.toordinal)

X = data.drop('Lead Time', axis=1)
y = data['Lead Time']

categorical_cols = [c for c in ['Factory', 'Region', 'Ship Mode'] if c in X.columns]

preprocessor = ColumnTransformer(
    transformers=[('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)],
    remainder='passthrough'
)
X_processed = preprocessor.fit_transform(X)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_processed, y)

joblib.dump(model, 'model.pkl')
joblib.dump(preprocessor, 'preprocessor.pkl')
joblib.dump(X.columns, 'columns.pkl')

print("model trained")
>>>>>>> cc7ccdd2d1c495804b086cae34a573a05be36310
