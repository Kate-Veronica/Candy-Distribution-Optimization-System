import streamlit as st
import pandas as pd
import pickle

st.title("Nassau Candy Prediction Dashboard")

uploaded_file = st.file_uploader("Upload your cleaned CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    TARGET_COLUMN = 'Sales'  # replace with your target column
    if TARGET_COLUMN not in data.columns:
        st.error(f"Target column '{TARGET_COLUMN}' not found in CSV!")
    else:
        X = data.drop(TARGET_COLUMN, axis=1)
        y = data[TARGET_COLUMN]

        st.write("Data Preview:")
        st.dataframe(data.head())

        try:
            with open("model.pkl", "rb") as f:
                saved = pickle.load(f)
                model = saved['model']
                encoders = saved['encoders']
                model_columns = saved['columns']
        except FileNotFoundError:
            st.error("Model file 'model.pkl' not found!")
            st.stop()

        for col, le in encoders.items():
            if col in X.columns:
                X[col] = le.transform(X[col])

        st.write("Select feature values to predict Sales:")
        input_data = {}
        for col in model_columns:
            if col in X.columns:
                if pd.api.types.is_numeric_dtype(X[col]):
                    input_data[col] = st.number_input(f"{col}", float(X[col].min()), float(X[col].max()), float(X[col].mean()))
                else:
                    input_data[col] = st.selectbox(f"{col}", X[col].unique())
            else:
                input_data[col] = 0

        input_df = pd.DataFrame([input_data])

        if st.button("Predict Sales"):
            prediction = model.predict(input_df)
            st.success(f"Predicted Sales: {prediction[0]:.2f}")

else:
    st.info("Please upload a cleaned CSV file to start.")