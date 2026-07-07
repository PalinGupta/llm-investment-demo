import re
from services.historical_data import load_stock_history
from services.trade_simulator import simulate_trades


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

    trade_returns = simulate_trades(
    stock,
    direction,
    target_price,
    )

    trades = len(trade_returns)

    winning_trades = sum(
        1 for trade in trade_returns if trade > 0
    )

    if trades > 0:

        win_rate = round(
            (winning_trades / trades) * 100,
            2,
        )

        total_return = round(
            sum(trade_returns),
            2,
        )

        max_drawdown = round(
            abs(min(trade_returns)),
            2,
        )

    else:

        win_rate = 0
        total_return = 0
        max_drawdown = 0

    return {
        "current_price": current_price,
        "signal": signal,
        "backtest": {
            "trades": trades,
            "winning_trades": winning_trades,
            "win_rate": f"{win_rate}%",
            "total_return": f"{total_return}%",
            "max_drawdown": f"{max_drawdown}%",
        },
    }