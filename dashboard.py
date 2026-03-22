import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Nassau Candy Dashboard", layout="wide")

st.title("Nassau Candy Distribution Dashboard")
st.markdown("Analyze sales performance and generate predictions for optimized decision-making.")

@st.cache_data
def load_data(path="cleaned_data.csv"):
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    return df

data = load_data()

@st.cache_resource
def load_model(path="model.pkl"):
    with open(path, "rb") as f:
        return pickle.load(f)

model = load_model()

st.sidebar.header("Filter Options")

category_col = "Category" if "Category" in data.columns else data.columns[0]
region_col = "Region" if "Region" in data.columns else data.columns[1]

selected_category = st.sidebar.selectbox("Select Category", data[category_col].dropna().unique())
selected_region = st.sidebar.selectbox("Select Region", data[region_col].dropna().unique())

@st.cache_data
def filter_data(category, region):
    exact_match = data[(data[category_col] == category) & (data[region_col] == region)]
    if not exact_match.empty:
        return exact_match
    partial_match = data[(data[category_col] == category) | (data[region_col] == region)]
    if not partial_match.empty:
        return partial_match
    return data  

filtered_data = filter_data(selected_category, selected_region)

if filtered_data.empty:
    st.warning("No data available for selected filters. Showing closest matches.")

@st.cache_data
def get_predictions(filtered_df):
    df = filtered_df.copy()

    drop_cols = ["Row ID", "Order ID", "Customer ID", "Postal Code"]
    df = df.drop(columns=[col for col in drop_cols if col in df.columns], errors='ignore')

    df = pd.get_dummies(df, drop_first=True)

    df = df.apply(pd.to_numeric, errors='coerce').fillna(0)

    model_features = model.feature_names_in_
    for col in model_features:
        if col not in df.columns:
            df[col] = 0

    df = df[model_features]

    return model.predict(df)

try:
    predictions = get_predictions(filtered_data)
    filtered_data = filtered_data.copy()
    filtered_data["Predicted Sales"] = predictions
except:
    st.error("Prediction error. Please check model compatibility.")
    predictions = []

st.subheader("Filtered Data")

display_cols = ['Product Name', 'Category', 'Region', 'Units', 'Sales']
display_cols = [col for col in display_cols if col in filtered_data.columns]

st.dataframe(filtered_data[display_cols], use_container_width=True)

st.subheader("Predictions")

display_cols_pred = ['Product Name', 'Category', 'Region', 'Units', 'Sales', 'Predicted Sales']
display_cols_pred = [col for col in display_cols_pred if col in filtered_data.columns]

st.dataframe(filtered_data[display_cols_pred], use_container_width=True)

st.markdown("---")
st.subheader("Sales vs Predicted Sales")

if "Predicted Sales" in filtered_data.columns:
    chart_data = filtered_data[['Product Name', 'Sales', 'Predicted Sales']].copy()
    chart_data = chart_data.head(10)
    chart_data = chart_data.set_index('Product Name')
    st.bar_chart(chart_data)

st.subheader("Download Results")

st.download_button(
    label="Download Filtered Data",
    data=filtered_data.to_csv(index=False).encode("utf-8"),
    file_name="filtered_data.csv",
    mime="text/csv"
)

st.download_button(
    label="Download Predictions",
    data=filtered_data.to_csv(index=False).encode("utf-8"),
    file_name="predictions.csv",
    mime="text/csv"
)