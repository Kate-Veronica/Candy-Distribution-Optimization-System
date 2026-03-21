# Candy-Distribution-Optimization-System

## Overview:
This project predicts sales for Nassau Candy Distributor based on historical order data. Using a trained **Linear Regression model**, the system provides an interactive **Streamlit dashboard** that allows users to filter data, view analytics, and generate sales predictions in real-time.

The dashboard is robust and user-friendly:
- Handles all Category + Region selections, including unmatched or empty combinations.
- Automatically shows closest matching data when exact matches are not available.
- Optimized with caching for fast filter updates and predictions.

## Features
- Predicts sales for each order based on multiple features.
- Interactive filters for **Category** and **Region**.
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
- Provides accurate sales predictions using historical order data.
- Non-technical users can run simulations via CSV upload and manual filter selections.
- Supports data-driven decisions for inventory and shipping optimization.
- Fully interactive and robust dashboard, ready for deployment.
  
## Links
- Research Paper [https://docs.google.com/document/d/1qUIPZKaygyPB_RfvLSIYMbLNHWF0v3VN3wOAtoewQZE/edit?usp=drive_link]
- Deployed Dashboard: [https://candy-distribution-optimization-system-bptixedttq4laxkvewq9kv.streamlit.app/]
- Project Feedback Video: []

## Conclusion
This system provides an easy-to-use, interactive prediction dashboard for Nassau Candy Distributor, enabling data-driven decisions, reducing errors, and optimizing operational efficiency.
