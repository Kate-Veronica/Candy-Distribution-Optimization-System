import streamlit as st
import pandas as pd
import pickle
import numpy as np

st.set_page_config(page_title="Nassau Candy Prediction Dashboard", layout="wide")
st.title("Nassau Candy Prediction Dashboard")

try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("columns.pkl", "rb") as f:
        columns = pickle.load(f)
    with open("encoders.pkl", "rb") as f:
        encoders = pickle.load(f)
except FileNotFoundError:
    st.error("Model files not found. Ensure 'model.pkl', 'columns.pkl', and 'encoders.pkl' are in the same folder.")
    st.stop()

uploaded_file = st.file_uploader("Upload your cleaned CSV", type="csv")

if uploaded_file:
    try:
        data = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Error reading CSV file: {e}")
        st.stop()

    missing_cols = [c for c in columns if c not in data.columns]
    if missing_cols:
        st.error(f"Missing columns in CSV: {missing_cols}")
        st.stop()

    X = data[columns].copy()

    for col, le in encoders.items():
        if col in X.columns:
            X[col] = X[col].map(lambda x: le.transform([x])[0] if x in le.classes_ else -1)

    try:
        predictions = model.predict(X)
        data["Predicted Sales"] = predictions
        st.success("✅ Predictions completed!")
        st.dataframe(data)
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        st.stop()
else:
    st.info("Please upload a cleaned CSV file to get predictions.")

st.subheader("Enter values for a single prediction")

categorical_cols = ["Ship Mode", "Country/Region", "City", "State/Province",
                    "Division", "Region", "Product Name"]

input_data = {}

for col in columns:
    if col in categorical_cols:
        if uploaded_file:
            options = sorted(data[col].dropna().unique())
        else:
            options = ["Option1", "Option2", "Option3"]  
        input_data[col] = st.selectbox(col, options=options)
    else:
        input_data[col] = st.number_input(col, value=0)

if st.button("Predict Single Row"):
    try:
        input_df = pd.DataFrame([input_data])

        for col, le in encoders.items():
            if col in input_df.columns:
                input_df[col] = input_df[col].map(
                    lambda x: le.transform([x])[0] if x in le.classes_ else -1
                )

        for col in input_df.columns:
            if col not in categorical_cols:
                input_df[col] = pd.to_numeric(input_df[col], errors='coerce').fillna(0)

        input_df = input_df[columns]

        pred = model.predict(input_df)
        st.success(f"Predicted Sales: {pred[0]:.2f}")
    except Exception as e:
        st.error(f"Error predicting single input: {e}")