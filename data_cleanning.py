import pandas as pd

data = pd.read_csv('Nassau Candy Distributor.csv')

data['Order Date'] = pd.to_datetime(data['Order Date'],dayfirst = True)
data['Ship Date'] = pd.to_datetime(data['Ship Date'],dayfirst = True)

data['Lead Time'] = (data['Ship Date'] - data['Order Date']).dt.days
data = data[data['Lead Time']>=0]

data.to_csv('cleaned_data.csv', index=False)

print("Cleaned data saved!")