import re


ACTION_MAP = {
    "BUY": "BUY",
    "PURCHASE": "BUY",
    "ACCUMULATE": "BUY",
    "ENTER": "BUY",
    "GO LONG": "BUY",

    "SELL": "SELL",
    "EXIT": "SELL",
    "BOOK PROFIT": "SELL",
    "TAKE PROFIT": "SELL",
    "CLOSE POSITION": "SELL",
}

STOCK_MAP = {
    "TCS": "TCS",

    "INFOSYS": "INFY",
    "INFY": "INFY",

    "RELIANCE": "RELIANCE",

    "ICICI BANK": "ICICIBANK",
    "ICICIBANK": "ICICIBANK",

    "HDFC BANK": "HDFCBANK",
    "HDFCBANK": "HDFCBANK",

    "SBI": "SBIN",
    "STATE BANK OF INDIA": "SBIN",
    "SBIN": "SBIN",
}


def normalize_strategy(parsed):

    action = parsed.get("action", "").upper().strip()
    action = ACTION_MAP.get(action, action)

    stock = parsed.get("stock", "").upper().strip()
    stock = STOCK_MAP.get(stock, stock)

    condition = parsed.get("condition", "").strip()

    lower = condition.lower()

    number = re.findall(r"\d+\.?\d*", condition)

    price = number[0] if number else ""

    if any(word in lower for word in [
        "above",
        "cross",
        "crosses",
        "greater",
        "break above",
    ]):
        condition = f"Price Above {price}"

    elif any(word in lower for word in [
        "below",
        "under",
        "less",
        "drop",
        "falls",
    ]):
        condition = f"Price Below {price}"

    return {
        "action": action,
        "stock": stock,
        "condition": condition,
    }