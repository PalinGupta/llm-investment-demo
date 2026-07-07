from services.analysis_generator import generate_analysis

backtest = {
    "trades": 42,
    "winning_trades": 28,
    "win_rate": "66.7%",
    "total_return": "18.4%",
    "max_drawdown": "7.2%",
}

analysis = generate_analysis(
    "Buy TCS above 4000",
    backtest,
)

print(analysis)