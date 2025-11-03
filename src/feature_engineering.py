import pandas as pd

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # Add tip_rate if columns exist
    if set(["total_bill","tip"]).issubset(df.columns):
        df["tip_rate"] = df["tip"] / df["total_bill"].replace(0, pd.NA)
        df["tip_rate"] = df["tip_rate"].fillna(0)
    # One-hot encode typical categoricals
    cat_cols = [c for c in ["sex","smoker","day","time"] if c in df.columns]
    if cat_cols:
        df = pd.get_dummies(df, columns=cat_cols, drop_first=True)
    return df
