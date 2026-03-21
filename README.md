# Candy-Distribution-Optimization-System

## Overview:
This project predicts sales for Nassau Candy Distributor based on historical order data. Using a trained Linear Regression model, the system allows users to upload a cleaned dataset, enter feature values, and obtain sales predictions through an interactive Streamlit dashboard.

## Features
- Predicts sales for each order based on multiple features.
- Supports CSV upload for batch predictions.
- Interactive input for manual feature testing.
- Displays predictions directly in the dashboard.

## Dataset
- **Source:** Historical orders from Nassau Candy Distributor.
- **Fields:** Row ID, Order ID, Order Date, Ship Date, Ship Mode, Customer ID, Country/Region, City, State/Province, Postal Code, Division, Region, Product ID, Product Name, Units, Gross Profit, Cost, Lead Time, Sales.  
- **Note:** Only the cleaned dataset (`cleaned_data.csv`) is included in the repository. Use this file to train and test the model.  
- **Optional:** You can replace it with your own CSV following the same schema.  
- **Download** (click here to download) 
  [https://drive.google.com/file/d/1IZjoQwuhbNZUnmMCL6j441tFoMkDEq-H/view?usp=drive_link]
- - You can also replace it with your own CSV following the same schema.

## How to Run
### 1. Install dependencies
```bash
pip install -r requirements.txt
```
### 2. Train the model
Run once to generate **model.pkl**:
```bash
python train_model.py
```
- This will load **cleaned_data.csv**, encode categorical features, train a Linear Regression model, and save the model and encoders to **model.pkl**.

### 3. Run the Streamlit dashboard
```bash
streamlit run model.py
```
- Upload cleaned_data.csv in the app.
- Enter values for features (numeric or select boxes for categories).
- Click Predict Sales to see the predicted output.

### Repository Structure
```bash
Project 1/
│
├─ train_model.py       # Script to train the Linear Regression model
├─ model.py             # Streamlit dashboard for predictions
├─ cleaned_data.csv     # Cleaned dataset
├─ model.pkl            # Trained model saved after training
├─ .gitignore           # Excludes model.pkl and cache
└─ README.md            # Project instructions
```

## Technology Stack
- Python 3.13
- Pandas, NumPy
- Scikit-learn (Linear Regressor)
- Streamlit for dashboard

## Project Outcome
- Predicts sales accurately using historical order data.
- Allows non-technical users to run simulations via CSV upload and manual input.
- Supports decision-making by providing actionable predictions for inventory and shipping planning.
  
## Links
- Research Paper [https://docs.google.com/document/d/1qUIPZKaygyPB_RfvLSIYMbLNHWF0v3VN3wOAtoewQZE/edit?usp=drive_link]
- Deployed Dashboard:
- Project Feedback Video: 

## Conclusion
This system provides an easy-to-use prediction dashboard for Nassau Candy Distributor, enabling data-driven decisions to optimize sales, reduce errors, and improve operational efficiency.
