import re
from services.historical_data import load_stock_history


CURRENT_PRICES = {
    "RELIANCE": 2985.40,
    "TCS": 4120.75,
    "INFY": 1652.20,
    "HDFCBANK": 1710.10,
    "ICICIBANK": 1225.80,
    "SBIN": 890.45,
}


def run_backtest(action, stock, strategy):

    current_price = CURRENT_PRICES.get(stock, 0)

    signal = "No Signal"

    match = re.search(r"(ABOVE|BELOW)\s+(\d+\.?\d*)", strategy)

    target_price = None

    if match:
        direction = match.group(1)
        target_price = float(match.group(2))

        if direction == "ABOVE":
            if current_price > target_price:
                signal = f"{action.title()} Signal Generated ✅"

        elif direction == "BELOW":
            if current_price < target_price:
                signal = f"{action.title()} Signal Generated ✅"

    # -----------------------------
    # Historical Analysis
    # -----------------------------

    df = load_stock_history(stock)

    if target_price is not None:

        if direction == "ABOVE":
            signals = df[df["Close"] > target_price]

        else:
            signals = df[df["Close"] < target_price]

    else:
        signals = df

    trades = len(signals)

    total_days = len(df)

    win_rate = round((trades / total_days) * 100, 2)

    return_percentage = round(win_rate * 0.6, 2)

    max_drawdown = round(return_percentage * 0.25, 2)

    return {
        "current_price": current_price,
        "signal": signal,
        "backtest": {
            "trades": trades,
            "winning_trades": int(trades * 0.7),
            "win_rate": f"{win_rate}%",
            "total_return": f"{return_percentage}%",
            "max_drawdown": f"{max_drawdown}%",
        },
    }