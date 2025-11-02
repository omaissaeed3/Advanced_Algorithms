import pandas as pd
from eda import run_eda
from cleaning import clean_data
from feature_engineering import engineer_features
from scaling import scale_features

DATA_PATH = "data/input.csv"  # update path if needed

def main():
    df = pd.read_csv(DATA_PATH)
    df = run_eda(df)
    df = clean_data(df)
    df = engineer_features(df)
    df = scale_features(df)
    print("Pipeline finished successfully. Rows:", len(df))

if __name__ == "__main__":
    main()
