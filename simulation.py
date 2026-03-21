<<<<<<< HEAD
import pandas as pd

def simulate_factories(sample, factories, model, preprocessor, columns):
    results = []

    for factory in factories:
        temp = sample.copy()

        factory_cols = [c for c in columns if c.startswith("Factory_")]
        for col in factory_cols:
            temp[col] = 0

        col_name = f"Factory_{factory}"
        if col_name in columns:
            temp[col_name] = 1

        for col in columns:
            if col not in temp:
                temp[col] = 0

        temp_df = pd.DataFrame([temp])
        temp_df = temp_df[columns]

        X_temp = preprocessor.transform(temp_df)

        pred = model.predict(X_temp)[0]

        results.append((factory, round(pred, 2)))

=======
import pandas as pd

def simulate_factories(sample, factories, model, preprocessor, columns):
    results = []

    for factory in factories:
        temp = sample.copy()

        factory_cols = [c for c in columns if c.startswith("Factory_")]
        for col in factory_cols:
            temp[col] = 0

        col_name = f"Factory_{factory}"
        if col_name in columns:
            temp[col_name] = 1

        for col in columns:
            if col not in temp:
                temp[col] = 0

        temp_df = pd.DataFrame([temp])
        temp_df = temp_df[columns]

        X_temp = preprocessor.transform(temp_df)

        pred = model.predict(X_temp)[0]

        results.append((factory, round(pred, 2)))

>>>>>>> b0cebfcab0cc1590f77ae1b6a07f220c5a876ad6
    return results