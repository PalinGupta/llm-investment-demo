from services.historical_data import load_stock_history


def simulate_trades(stock, direction, target_price):

    df = load_stock_history(stock)

    trades = []

    HOLD_DAYS = 10

    for i in range(len(df) - HOLD_DAYS):

        close_price = df.iloc[i]["Close"]

        if direction == "ABOVE":

            if close_price > target_price:

                entry = close_price
                exit_price = df.iloc[i + HOLD_DAYS]["Close"]

                profit = ((exit_price - entry) / entry) * 100

                trades.append(profit)

        elif direction == "BELOW":

            if close_price < target_price:

                entry = close_price
                exit_price = df.iloc[i + HOLD_DAYS]["Close"]

                profit = ((exit_price - entry) / entry) * 100

                trades.append(profit)

    return trades