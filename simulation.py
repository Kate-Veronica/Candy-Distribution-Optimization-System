import pandas as pd
import joblib

def simulate_factories(sample, factories, model, preprocessor, columns):
    results = []
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
        X_temp = preprocessor.transform(temp_df)
        pred = model.predict(X_temp)[0]
        results.append((factory, round(pred, 2)))
    return results