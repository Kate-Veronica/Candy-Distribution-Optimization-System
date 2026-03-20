<<<<<<< HEAD
import pandas as pd

data = pd.read_csv('Nassau Candy Distributor.csv')

data['Order Date'] = pd.to_datetime(data['Order Date'],dayfirst = True)
data['Ship Date'] = pd.to_datetime(data['Ship Date'],dayfirst = True)

data['Lead Time'] = (data['Ship Date'] - data['Order Date']).dt.days
data = data[data['Lead Time']>=0]

data.to_csv('cleaned_data.csv', index=False)

=======
import pandas as pd

data = pd.read_csv('Nassau Candy Distributor.csv')

data['Order Date'] = pd.to_datetime(data['Order Date'],dayfirst = True)
data['Ship Date'] = pd.to_datetime(data['Ship Date'],dayfirst = True)

data['Lead Time'] = (data['Ship Date'] - data['Order Date']).dt.days
data = data[data['Lead Time']>=0]

data.to_csv('cleaned_data.csv', index=False)

>>>>>>> cc7ccdd2d1c495804b086cae34a573a05be36310
print("Cleaned data saved!")