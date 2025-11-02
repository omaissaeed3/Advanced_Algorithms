import pandas as pd

def run_eda(df: pd.DataFrame) -> pd.DataFrame:
    print(df.head())
    print(df.info())
    return df
