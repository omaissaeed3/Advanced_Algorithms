import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # Drop fully empty rows
    df.dropna(how="all", inplace=True)
    # Fill numeric NA with median
    for col in df.select_dtypes(include="number").columns:
        if df[col].isna().any():
            df[col] = df[col].fillna(df[col].median())
    # Robust outlier trimming with IQR (3x)
    for col in df.select_dtypes(include="number").columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 3*iqr
        upper = q3 + 3*iqr
        df = df[(df[col] >= lower) & (df[col] <= upper)]
    return df.reset_index(drop=True)
