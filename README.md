# Factory Reallocation & Sales Optimization System – Nassau Candy Distributor

## Overview:
This project predicts sales for Nassau Candy Distributor based on historical order data and provides an **interactive Streamlit dashboard** for decision-making. Users can explore different product, category, and region combinations, generate predictions, and download results for analysis. The system supports **scenario simulations** and robust handling of unmatched or empty filters.

## Features
- Predicts sales for each order based on multiple features.
- Interactive filters for **Category**,**Region** and **Ship Mode**.
- Displays predictions directly in the dashboard.
- Downloadable CSVs for **filtered data** and **predictions**.
- Handles edge cases with unmatched filters gracefully.
- Supports CSV upload for batch predictions (optional).

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
streamlit run model.py
```
- Use sidebar filters to select Category and Region.
- View predictions directly in the dashboard.
- Download filtered data and predictions as CSV files.

### Repository Structure
```bash
Project 1/
│
├─ train_model.py       # Script to train the Linear Regression model
├─ dashboard.py         # Streamlit dashboard for predictions
├─ cleaned_data.csv     # Cleaned dataset
├─ model.pkl            # Trained model saved after training
├─ requirements.txt     # Python dependencies
└─ README.md            # Project instructions
```

## Technology Stack
- Python 3.13
- Pandas, NumPy
- Scikit-learn (Linear Regressor)
- Streamlit for dashboard and deployment

## Project Outcome
- Provides accurate sales predictions for all product-category-region combinations.
- Dashboard supports scenario simulations and data-driven decision-making.
- Downloadable outputs for reporting and analysis.
- Robust and user-friendly system, optimized for fast interactions.
  
## Links
- Research Paper [https://docs.google.com/document/d/1qUIPZKaygyPB_RfvLSIYMbLNHWF0v3VN3wOAtoewQZE/edit?usp=drive_link]
- Deployed Dashboard: [https://candy-distribution-optimization-system-bptixedttq4laxkvewq9kv.streamlit.app/]
- Project Feedback Video: []

## Conclusion
This system provides an interactive, predictive dashboard that transforms Nassau Candy Distributor’s operations from static analytics to intelligent, actionable decision-making. By forecasting sales and recommending optimized product assignments, it improves efficiency, profitability, and operational insight, while remaining user-friendly, scalable, and robust.
