def parse_strategy(strategy: str):
    strategy = strategy.upper()

    action = "UNKNOWN"
    stock = "UNKNOWN"
    condition = "UNKNOWN"

    if "BUY" in strategy:
        action = "BUY"
    elif "SELL" in strategy:
        action = "SELL"

    stocks = [
        "RELIANCE",
        "TCS",
        "INFY",
        "HDFCBANK",
        "ICICIBANK",
        "SBIN",
    ]

    for s in stocks:
        if s in strategy:
            stock = s
            break

    if "ABOVE" in strategy:
        price = strategy.split("ABOVE")[-1].strip()
        condition = f"Price Above {price}"

    elif "BELOW" in strategy:
        price = strategy.split("BELOW")[-1].strip()
        condition = f"Price Below {price}"

    return {
        "action": action,
        "stock": stock,
        "condition": condition,
    }