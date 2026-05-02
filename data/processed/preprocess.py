import pandas as pd
from pathlib import Path

PROCESSED_DIR = Path(__file__).resolve().parent
OUTPUT_PATH = PROCESSED_DIR / "preprocessed_data.csv"

def preprocess(df):
    # convertir la colonne "date" en format datetime
    df["date"] = pd.to_datetime(df["date"])

    
    nb_doublons = df.duplicated().sum()
    df = df.drop_duplicates()
    print(f"Nombre de doublons supprimes: {nb_doublons}")

    df.to_csv(OUTPUT_PATH, index=False)

    return df
