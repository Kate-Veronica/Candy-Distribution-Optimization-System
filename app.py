import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Nassau Candy Project", layout="wide")
st.title("Nassau Candy Distribution Project")

try:
    model = joblib.load("model.pkl")
    st.success("✅ Model loaded successfully!")
except:
    st.warning("⚠️ Model file not found. Upload model.pkl to your repo.")

try:
    data = pd.read_csv("cleaned_data.csv")
    st.write("### Sample of Cleaned Data")
    st.dataframe(data.head())
except:
    st.warning("⚠️ cleaned_data.csv not found. Upload cleaned_data.csv to your repo.")

st.write("### Make a Prediction")
input_value = st.number_input("Enter a value", min_value=0, max_value=1000)

if st.button("Predict"):
    try:
        prediction = model.predict([[input_value]])
        st.success(f"Prediction: {prediction[0]}")
    except:
        st.error("⚠️ Error in prediction. Check your model or input format.")