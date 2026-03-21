import streamlit as st
import pandas as pd
import joblib
import numpy as np

model = joblib.load("lead_time_model.pkl")

st.title("Nassau Candy Factory Optimization Simulator")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.write("Preview of uploaded data:")
    st.dataframe(data.head())

    for col in ['Order Date', 'Ship Date']:
        if col in data.columns:
            data[col] = pd.to_datetime(data[col], errors='coerce')

    if 'Lead Time' not in data.columns and 'Order Date' in data.columns and 'Ship Date' in data.columns:
        data['Lead Time'] = (data['Ship Date'] - data['Order Date']).dt.days

    required_columns = ['Lead Time']   

    for col in required_columns:
        if col not in data:
            data[col] = 0

    X = data[required_columns]

    X = X.apply(pd.to_numeric, errors='coerce').fillna(0)

    predictions = model.predict(X)

    data['Predicted Lead Time'] = predictions

    st.write("Predicted Lead Time:")
    st.dataframe(data[['Predicted Lead Time']])

    csv = data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download predictions as CSV",
        data=csv,
        file_name='predicted_lead_times.csv',
        mime='text/csv',
    )