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
except FileNotFoundError:
    st.error("Model files not found. Ensure 'model.pkl' and 'columns.pkl' are in the same folder.")
    st.stop()

uploaded_file = st.file_uploader("Upload your cleaned CSV", type="csv")

if uploaded_file:
    try:
        data = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Error reading CSV file: {e}")
        st.stop()

    missing_cols = [col for col in columns if col not in data.columns]
    if missing_cols:
        st.error(f"Missing columns in CSV: {missing_cols}")
        st.stop()

    X = data[columns].copy()

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

st.subheader("Enter values for prediction manually")

input_data = {}
for col in columns:
    input_data[col] = st.text_input(col, "")

if st.button("Predict Sales for Single Input"):
    try:
        input_df = pd.DataFrame([input_data])
        input_df = input_df.astype(float)
        pred = model.predict(input_df)
        st.success(f"Predicted Sales: {pred[0]:.2f}")
    except Exception as e:
        st.error(f"Error predicting single input: {e}")