import streamlit as st
import pandas as pd
import pickle

@st.cache_data
def load_data(path="cleaned_data.csv"):
    df = pd.read_csv(path)
    return df

data = load_data()

@st.cache_resource
def load_model(path="model.pkl"):
    with open(path, "rb") as f:
        return pickle.load(f)

model = load_model()

st.sidebar.header("Filter Options")

selected_category = st.sidebar.selectbox("Select Category", data["Category"].unique())
selected_region = st.sidebar.selectbox("Select Region", data["Region"].unique())

@st.cache_data
def filter_data(category, region):
    return data[(data["Category"] == category) & (data["Region"] == region)]

filtered_data = filter_data(selected_category, selected_region)

@st.cache_data
def get_predictions(filtered_df):
    features = filtered_df.drop(columns=["TargetColumn"], errors="ignore")
    return model.predict(features)

predictions = get_predictions(filtered_data)

st.title("Nassau Candy Dashboard")

st.subheader("Filtered Data")
st.dataframe(filtered_data.head(100))  

st.subheader("Predictions")
st.write(predictions)

st.download_button(
    label="Download Filtered Data",
    data=filtered_data.to_csv(index=False).encode("utf-8"),
    file_name="filtered_data.csv",
    mime="text/csv"
)

st.download_button(
    label="Download Predictions",
    data=pd.DataFrame(predictions, columns=["Prediction"]).to_csv(index=False).encode("utf-8"),
    file_name="predictions.csv",
    mime="text/csv"
)