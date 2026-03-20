<<<<<<< HEAD
import streamlit as st
import pandas as pd
import joblib

def simulate_factories(sample, factories, model, preprocessor, columns):
    results = []
    for col in ['Order Date', 'Ship Date']:
        if col in sample.index:
            sample[col] = pd.to_datetime(sample[col]).toordinal()
    for factory in factories:
        temp = sample.copy()
        factory_cols = [c for c in columns if c.startswith("Factory_")]
        for col in factory_cols:
            temp[col] = 0
        col_name = f"Factory_{factory}"
        temp[col_name] = 1
        for col in columns:
            if col not in temp:
                temp[col] = 0
        temp_df = pd.DataFrame([temp])
        if preprocessor:
            X_temp = preprocessor.transform(temp_df)
        else:
            X_temp = temp_df[columns]
        pred = model.predict(X_temp)[0]
        results.append((factory, round(pred, 2)))
    return results

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

selected_product = st.sidebar.selectbox(
    "Select Product", product_list,
    format_func=lambda x: x if not x.startswith("--") else "Select Product"
)
selected_region = st.sidebar.selectbox(
    "Select Region", region_list,
    format_func=lambda x: x if not x.startswith("--") else "Select Region"
)
selected_ship_mode = st.sidebar.selectbox(
    "Select Ship Mode", ship_mode_list,
    format_func=lambda x: x if not x.startswith("--") else "Select Ship Mode"
)


if st.button("Run Simulation"):
    if selected_product.startswith("--") or selected_region.startswith("--") or selected_ship_mode.startswith("--"):
        st.warning("⚠️ Please select Product, Region, and Ship Mode before running simulation.")
    else:
        filtered = data[(data['Product Name'] == selected_product) &
                        (data['Region'] == selected_region) &
                        (data['Ship Mode'] == selected_ship_mode)]
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
=======
import streamlit as st
import pandas as pd
import joblib

def simulate_factories(sample, factories, model, preprocessor, columns):
    results = []
    for col in ['Order Date', 'Ship Date']:
        if col in sample.index:
            sample[col] = pd.to_datetime(sample[col]).toordinal()
    for factory in factories:
        temp = sample.copy()
        factory_cols = [c for c in columns if c.startswith("Factory_")]
        for col in factory_cols:
            temp[col] = 0
        col_name = f"Factory_{factory}"
        temp[col_name] = 1
        for col in columns:
            if col not in temp:
                temp[col] = 0
        temp_df = pd.DataFrame([temp])
        if preprocessor:
            X_temp = preprocessor.transform(temp_df)
        else:
            X_temp = temp_df[columns]
        pred = model.predict(X_temp)[0]
        results.append((factory, round(pred, 2)))
    return results

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

selected_product = st.sidebar.selectbox(
    "Select Product", product_list,
    format_func=lambda x: x if not x.startswith("--") else "Select Product"
)
selected_region = st.sidebar.selectbox(
    "Select Region", region_list,
    format_func=lambda x: x if not x.startswith("--") else "Select Region"
)
selected_ship_mode = st.sidebar.selectbox(
    "Select Ship Mode", ship_mode_list,
    format_func=lambda x: x if not x.startswith("--") else "Select Ship Mode"
)


if st.button("Run Simulation"):
    if selected_product.startswith("--") or selected_region.startswith("--") or selected_ship_mode.startswith("--"):
        st.warning("⚠️ Please select Product, Region, and Ship Mode before running simulation.")
    else:
        filtered = data[(data['Product Name'] == selected_product) &
                        (data['Region'] == selected_region) &
                        (data['Ship Mode'] == selected_ship_mode)]
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
>>>>>>> cc7ccdd2d1c495804b086cae34a573a05be36310
st.map(factory_df.rename(columns={'lat':'latitude','lon':'longitude'}))