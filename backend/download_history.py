import os
import yfinance as yf

STOCKS = {
    "TCS": "TCS.NS",
    "INFY": "INFY.NS",
    "RELIANCE": "RELIANCE.NS",
    "ICICIBANK": "ICICIBANK.NS",
    "HDFCBANK": "HDFCBANK.NS",
    "SBIN": "SBIN.NS",
}

output_folder = "data/history"
os.makedirs(output_folder, exist_ok=True)

for symbol, ticker in STOCKS.items():
    print(f"Downloading {symbol}...")

    df = yf.download(
        ticker,
        period="5y",
        interval="1d",
        auto_adjust=True,
        progress=False,
    )

    # Flatten MultiIndex columns if present
    if hasattr(df.columns, "nlevels") and df.columns.nlevels > 1:
        df.columns = df.columns.get_level_values(0)

    # Reset index so Date becomes a column
    df = df.reset_index()

    # Keep only required columns
    df = df[["Date", "Open", "High", "Low", "Close", "Volume"]]

    file_path = os.path.join(output_folder, f"{symbol}.csv")
    df.to_csv(file_path, index=False)

    print(f"Saved -> {file_path}")

print("\n✅ Historical data downloaded successfully!")