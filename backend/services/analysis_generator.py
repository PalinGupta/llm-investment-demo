import ollama


def generate_analysis(strategy, backtest):

    prompt = f"""
You are a financial analyst.

A user tested the following investment strategy:

{strategy}

Backtest Results:

Trades Executed: {backtest['trades']}
Winning Trades: {backtest['winning_trades']}
Win Rate: {backtest['win_rate']}
Total Return: {backtest['total_return']}
Maximum Drawdown: {backtest['max_drawdown']}

Write a short explanation (100-150 words).

Explain:
- Overall performance
- Risk level
- Strengths
- Weaknesses

Do not use bullet points.
Use simple English.
"""

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response["message"]["content"]