import pandas as pd
from pathlib import Path
from data.processed.preprocess import preprocess

PROJECT_ROOT = Path(__file__).resolve().parent
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "predictive_maintenance_dataset.csv"

def load_data():
    df = pd.read_csv(DATA_PATH)
    return df

if __name__ == "__main__":
    df = load_data()
    print(df.head())
    print(df.info())
    df1 = preprocess(df)
    print(df1.head())    
    print(df1.info())
