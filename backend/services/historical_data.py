import os
import pandas as pd

DATA_FOLDER = "data/history"


def load_stock_history(symbol: str):
    file_path = os.path.join(DATA_FOLDER, f"{symbol}.csv")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No historical data found for {symbol}")

    df = pd.read_csv(file_path)

    numeric_columns = ["Open", "High", "Low", "Close", "Volume"]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna().reset_index(drop=True)

    return df