import streamlit as st
import pandas as pd
import pickle

@st.cache_data
def load_data(path="cleaned_data.csv"):
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    return df

data = load_data()

st.write("Columns in dataset:", data.columns.tolist())

@st.cache_resource
def load_model(path="model.pkl"):
    with open(path, "rb") as f:
        return pickle.load(f)

model = load_model()

st.sidebar.header("Filter Options")

category_col = "Category" if "Category" in data.columns else data.columns[0]
region_col = "Region" if "Region" in data.columns else data.columns[1]

selected_category = st.sidebar.selectbox("Select Category", data[category_col].unique())
selected_region = st.sidebar.selectbox("Select Region", data[region_col].unique())

@st.cache_data
def filter_data(category, region):
    return data[(data[category_col] == category) & (data[region_col] == region)]

filtered_data = filter_data(selected_category, selected_region)

@st.cache_data
def get_predictions(filtered_df):
    if filtered_df.empty:
        return pd.Series([], dtype=float)
    for col in model.feature_names_in_:
        if col not in filtered_df.columns:
            filtered_df[col] = 0
    features = filtered_df[model.feature_names_in_]
    features = features.apply(pd.to_numeric, errors='coerce').fillna(0)
    return model.predict(features)

predictions = get_predictions(filtered_data)

st.title("Nassau Candy Dashboard")
st.subheader("Filtered Data")
if filtered_data.empty:
    st.write("No data available for the selected Category and Region.")
else:
    st.dataframe(filtered_data.head(100))

st.subheader("Predictions")
if filtered_data.empty:
    st.write("No predictions available for the selected Category and Region.")
else:
    st.write(predictions)

st.download_button(
    label="Download Filtered Data",
    data=filtered_data.to_csv(index=False).encode("utf-8"),
    file_name="filtered_data.csv",
    mime="text/csv"
)

if not filtered_data.empty:
    st.download_button(
        label="Download Predictions",
        data=pd.DataFrame(predictions, columns=["Prediction"]).to_csv(index=False).encode("utf-8"),
        file_name="predictions.csv",
        mime="text/csv"
    )