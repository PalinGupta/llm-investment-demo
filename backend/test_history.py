from services.historical_data import load_stock_history

df = load_stock_history("TCS")

print(df.head())

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)