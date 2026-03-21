import streamlit as st
import pandas as pd
import joblib
from simulation import simulate_factories

st.set_page_config(page_title="Nassau Candy Dashboard", layout="wide")
st.title("Nassau Candy Factory Optimization Simulator")

data = pd.read_csv("cleaned_data.csv")
data.columns = data.columns.str.strip()
model = joblib.load("model.pkl")

try:
    preprocessor = joblib.load("preprocessor.pkl")
except:
    preprocessor = None

columns = joblib.load("columns.pkl")

factory_columns = [c for c in columns if c.startswith("Factory_")]
factories = [c.replace("Factory_", "") for c in factory_columns]
if not factories:
    factories = ["Lot's O' Nuts", "Wicked Choccy's", "Sugar Shack", "Secret Factory", "The Other Factory"]

product_list = ["-- Select Product --"] + list(data['Product Name'].unique()) if 'Product Name' in data.columns else ["-- Select Product --"]
region_list = ["-- Select Region --"] + list(data['Region'].unique()) if 'Region' in data.columns else ["-- Select Region --"]
ship_mode_list = ["-- Select Ship Mode --"] + list(data['Ship Mode'].unique()) if 'Ship Mode' in data.columns else ["-- Select Ship Mode --"]

selected_product = st.sidebar.selectbox("Select Product", product_list)
selected_region = st.sidebar.selectbox("Select Region", region_list)
selected_ship_mode = st.sidebar.selectbox("Select Ship Mode", ship_mode_list)

if st.button("Run Simulation"):
    if selected_product.startswith("--") or selected_region.startswith("--") or selected_ship_mode.startswith("--"):
        st.warning("⚠️ Please select Product, Region, and Ship Mode before running simulation.")
    else:
        filtered = data[
            (data['Product Name'] == selected_product) &
            (data['Region'] == selected_region) &
            (data['Ship Mode'] == selected_ship_mode)
        ]
        sample = filtered.iloc[0] if not filtered.empty else data.iloc[0]
        results = simulate_factories(sample, factories, model, preprocessor, columns)
        df_results = pd.DataFrame(results, columns=['Factory', 'Predicted Lead Time']).sort_values(by='Predicted Lead Time')

        st.subheader("Factory Lead Time Predictions")
        st.dataframe(df_results)
        st.subheader("Lead Time Comparison")
        st.bar_chart(df_results.set_index('Factory')['Predicted Lead Time'])

        best = min(results, key=lambda x: x[1])
        st.success(f"✅ Best Factory: {best[0]}")

factory_df = pd.DataFrame({
    'Factory': factories,
    'lat': [32.881893, 32.076176, 48.11914, 41.446333, 35.1175],
    'lon': [-111.768036, -81.088371, -96.18115, -90.565487, -89.971107]
})
st.subheader("Factory Locations")
st.map(factory_df.rename(columns={'lat':'latitude','lon':'longitude'}))