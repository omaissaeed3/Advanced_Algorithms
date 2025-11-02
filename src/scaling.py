import pandas as pd
from sklearn.preprocessing import StandardScaler

def scale_features(df: pd.DataFrame, cols=None) -> pd.DataFrame:
    df = df.copy()
    if cols is None:
        cols = df.select_dtypes("number").columns.tolist()
    scaler = StandardScaler()
    df[cols] = scaler.fit_transform(df[cols])
    return df
