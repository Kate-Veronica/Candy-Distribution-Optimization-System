import pandas as pd

data = pd.read_csv("Nassau Candy Distributor.csv")

data['Order Date'] = pd.to_datetime(data['Order Date'], errors='coerce')
data['Ship Date'] = pd.to_datetime(data['Ship Date'], errors='coerce')

data = data.dropna(subset=['Order Date', 'Ship Date'])

data['Lead Time'] = (data['Ship Date'] - data['Order Date']).dt.days

data = data[data['Lead Time'] > 0]

data.reset_index(drop=True, inplace=True)

data.to_csv("cleaned_data.csv", index=False)

print("Data Cleaned")