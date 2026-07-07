from services.trade_simulator import simulate_trades

trades = simulate_trades(
    "TCS",
    "ABOVE",
    4000
)

print("Trades:", len(trades))

print()

print(trades[:10])