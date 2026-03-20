# Candy-Distribution-Optimization-System

## Overview:
This project simulates and recommends optimal product-to-factory assignments for Nassau Candy Distributor. Using historical order data, the system predicts lead times for different factory configurations and provides actionable recommendations to improve operational efficiency.

## Features
- Predicts shipping lead time for different factories.
- Simulates “what-if” scenarios for product reassignment.
- Visualizes lead time comparison using Streamlit.
- Optimized Random Forest model for deployment.

## Dataset
- **Source:** Historical orders from Nassau Candy Distributor.
- **Fields:** Order Date, Ship Date, Product, Factory, Region, Ship Mode, Sales, Units, Gross Profit, Cost, etc.
- **Note:** Dataset is not included in the repository due to size. You can replace it with your own CSV following the same schema.
- **Download** (click here to download) 
  [https://drive.google.com/file/d/1IZjoQwuhbNZUnmMCL6j441tFoMkDEq-H/view?usp=drive_link]
- - You can also replace it with your own CSV following the same schema.

## How to Run
### 1. Install dependencies
```bash
pip install -r requirements.txt
```
### 2. Run the dashboard
```bash
streamlit run dashboard.py
```
- Use the sidebar to select Product, Region, and Ship Mode.
- Click Run Simulation to see predicted lead times for all factories.
- The best factory will be highlighted automatically.

### 3. Notes
- Ensure **model.pkl** and columns.pkl are in the same directory as dashboard.py.
- The **.pkl** files are compressed Random Forest models for efficient predictions.

  Repository Structure
```bash
Project-1/
│
├─ model.py           # Trains and saves the Random Forest model
├─ dashboard.py       # Streamlit dashboard for simulation
├─ cleaned_data.csv   # Cleaned dataset
├─ model.pkl          # Compressed trained model
├─ columns.pkl        # Model feature columns
├─ requirements.txt   # Python dependencies
└─ README.md          # This file
```
## Technology Stack
- Python 3.13
- Pandas, NumPy
- Scikit-learn (Random Forest Regressor)
- Streamlit for dashboard

## Project Outcome
- Reduces shipping lead time through optimized factory assignments.
- Provides non-technical users a visual interface to simulate and compare scenarios.
- Decision intelligence approach helps balance speed, cost, and profitability.

### Links
- Research Paper:
- Deployed Dashboard:
- Project Feedback Video: 

### Conclusion
This system predicts lead times and recommends the best factory assignments, helping Nassau Candy Distributor improve shipping efficiency and profitability through data-driven decisions.
