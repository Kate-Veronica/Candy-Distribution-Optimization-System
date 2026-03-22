# Factory Reallocation & Sales Optimization System – Nassau Candy Distributor

## Overview:
This project predicts sales for Nassau Candy Distributor based on historical order data and provides an **interactive Streamlit dashboard** for decision-making. Users can explore different product, category, and region combinations, generate predictions, and download results for analysis. The system supports **scenario simulations** and robust handling of unmatched or empty filters.

## Features
- Predicts sales for selected products, categories, and regions.
- Interactive filters: Category, Region, Ship Mode.
- Real-time predictions displayed in the dashboard.
- Downloadable CSVs for filtered data and predictions.
- Visual comparison of actual vs predicted sales using bar charts.
- Automatically handles unmatched selections gracefully.
- Fast response using caching optimization.

## Dataset
- **Source:** Historical orders from Nassau Candy Distributor.
- **Fields:** Row ID, Order ID, Order Date, Ship Date, Ship Mode, Customer ID, Country/Region, City, State/Province, Postal Code, Division, Region, Product ID, Product Name, Units, Gross Profit, Cost, Lead Time, Sales.
- **Download** (click here to download) 
  [https://drive.google.com/file/d/1IZjoQwuhbNZUnmMCL6j441tFoMkDEq-H/view?usp=drive_link]
  - You can also replace it with your own CSV following the same schema.

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
- Loads **cleaned_data.csv**, encode categorical features, train a Linear Regression model, and saves **model.pkl**.

### 3. Run the Streamlit dashboard
```bash
streamlit run dashboard.py
```
- Use sidebar filters to select Category and Region.
- View predictions directly in the dashboard.
- Download filtered data and predictions as CSV files.

### Repository Structure
```bash
Project 1/
│
├─ train_model.py
├─  model.py
├─ dashboard.py         
├─ cleaned_data.csv     
├─ model.pkl         
├─ requirements.txt     
└─ README.md             
```

## Technology Stack
- Python 3.11
- Pandas, NumPy
- Scikit-learn (Linear Regressor)
- Streamlit for dashboard and deployment

## Project Outcome
- Accurate sales predictions for all product-category-region combinations.
- Supports scenario simulation and single-row predictions.
- Downloadable outputs for analysis and reporting.
- Robust, user-friendly, and optimized for fast interactions.
  
## Links
- Research Paper: [https://docs.google.com/document/d/1qUIPZKaygyPB_RfvLSIYMbLNHWF0v3VN3wOAtoewQZE/edit?usp=drive_link]
- Deployed Dashboard:
[https://candy-distribution-optimization-system-bptixedttq4laxkvewq9kv.streamlit.app/]
- Project Feedback Video:
[]

## Conclusion
This system transforms Nassau Candy Distributor’s operations from static analytics to intelligent, actionable decision-making, enabling optimized product assignments, improved efficiency, and operational insight.
