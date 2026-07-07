def normalize_action(action: str):

    action = action.upper().strip()

    buy_words = [
        "BUY",
        "PURCHASE",
        "ACCUMULATE",
        "ENTER",
        "GO LONG",
    ]

    sell_words = [
        "SELL",
        "EXIT",
        "BOOK PROFIT",
        "TAKE PROFIT",
        "CLOSE POSITION",
    ]

    if action in buy_words:
        return "BUY"

    if action in sell_words:
        return "SELL"

    return action