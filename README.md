# Factory Reallocation & Sales Optimization System – Nassau Candy Distributor

### DataSet:
[https://drive.google.com/file/d/15qNlSaU3emw8ex5S3kRg-4vlebQBKCsb/view?usp=drive_link]

### Live Dashboard: 
[https://candy-distribution-optimization-system-bptixedttq4laxkvewq9kv.streamlit.app/]

### Report Paper:
[https://docs.google.com/document/d/1qUIPZKaygyPB_RfvLSIYMbLNHWF0v3VN3wOAtoewQZE/edit?tab=t.0#heading=h.lxndaeizt6fd]

## Project Overview:
The project is to design a **decision intelligence system** for Nassau Candy Distributor to improve their allocation of products from factories and increase their shipping efficiency.

In contrast to traditional analytics, this system:
- Forecasts outcomes
- Runs simulations
- Enables data-informed decisions

## Business Problem
Static rules for assigning products to factories by Nassau Candy lead to the following effects:
- High shipping lead times  
- Inefficient routes  
- Erosion of profit margins

There is no system for simulating different reassignment scenarios, predicting the results of a process before it is executed, and optimizing decisions at scale.

## Solution Approach
The project proposes a **Predictive + Simulation-based Recommendation System**:

### 1. Predictive Layer
- Machine Learning model predicts **Sales performance**

### 2. Simulation Layer
- Tests multiple factory allocations
- Evaluates performance under different scenarios

### 3. Decision Layer
- Assists in the selection of the best factory assignments

## Technology Stack
- Python 
- Pandas, NumPy
- Scikit-learn 
- Streamlit
- Pickle / Joblib
  
## Project Workflow
### 1. Data Cleaning (data_cleaning.py)
- Convert date columns  
- Create Lead Time feature 
- Remove invalid/negative values

### 2. Model Training (train_model.py)
- Algorithm: Linear Regression  
- Target: Sales
- Label Encoding applied for categorical features  
- Model and encoders saved as `.pkl` files

### 3. Prediction System (model.py)
- Upload clean dataset  
- Apply encoding  
- Generate predictions  
- Capabilities:  
  - Bulk predictions
  - Single input prediction
 
### 4. Dashboard (dashboard.py)
- Interactive filtering:
  - Category  
  - Region  
- Displays:
  - Actual vs Predicted Sales  
- Visualizations:
  - Bar charts  
- Export:
  - Download predictions
 
### 5. Simulation Engine (simulation.py)
- Simulates product reassignment across factories  
- Predicts performance under each configuration
- Enables comparative analysis

## Key Features
- Sales Prediction Model
- Factory Reallocation Simulation
- Interactive Dashboard
- Sales vs Predicted Comparison
- CSV Export

## How to Run

### Install Dependencies
```
pip install -r requirements.txt
```
### 1. Clean data
```
python data_cleaning.py
```

### 2. Train Model
```
python train_model.py
```

### Run Dashboard
```
streamlit run dashboard.py
```

## Project Structure
```
├── data_cleaning.py       # Cleans raw data, computes Lead Time
├── train_model.py         # Trains Linear Regression model and saves model and encoders
├── model.pkl              # Trained ML model for predictions
├── columns.pkl            # Feature columns used in the model
├── encoders.pkl           # Encoders for categorical variables
├── dashboard.py           # Streamlit dashboard with filters, predictions, and charts
├── model.py               # Streamlit app for CSV upload and single/bulk predictions
├── simulation.py          # Simulates factory-product reassignments
├── app.py                 # Simple Streamlit preview and prediction interface
├── requirements.txt       # Python dependencies
├── runtime.txt            # Python version
```

## KPIs Tracked
- Lead Time Optimization (derived)
- Sales Prediction Accuracy
- Scenario Comparison Capability
- Decision Support Efficiency

## Future Enhancements
- Add Random Forest / Gradient Boosting
- Optimize based on Lead Time (core objective)
- Add factory coordinates for distance optimization
- Add recommendation ranking system

## Author
Kate Veronica Theetla
