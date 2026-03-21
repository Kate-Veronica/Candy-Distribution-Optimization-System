import streamlit as st
import pandas as pd
import pickle

st.title("Nassau Candy Prediction Dashboard")

uploaded_file = st.file_uploader("Upload your cleaned CSV", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    TARGET_COLUMN = 'Sales'
    if TARGET_COLUMN not in data.columns:
        st.error(f"Target column '{TARGET_COLUMN}' not found.")
    else:
        X = data.drop(TARGET_COLUMN, axis=1)
        y = data[TARGET_COLUMN]
        st.dataframe(data.head())

        try:
            with open("model.pkl", "rb") as f:
                saved = pickle.load(f)
                model = saved['model']
                encoders = saved['encoders']
                model_columns = saved['columns']
        except FileNotFoundError:
            st.error("model.pkl not found! Run training script first.")
            st.stop()

        for col, le in encoders.items():
            if col in X.columns:
                X[col] = le.transform(X[col])

        st.write("Enter values for prediction:")
        input_data = {}
        for col in model_columns:
            if col in X.columns:
                if pd.api.types.is_numeric_dtype(X[col]):
                    input_data[col] = st.number_input(
                        f"{col}",
                        float(X[col].min()),
                        float(X[col].max()),
                        float(X[col].mean())
                    )
                else:
                    input_data[col] = st.selectbox(f"{col}", X[col].unique())
            else:
                input_data[col] = 0

        input_df = pd.DataFrame([input_data])

        if st.button("Predict Sales"):
            prediction = model.predict(input_df)
            st.success(f"Predicted Sales: {prediction[0]:.2f}")