function BacktestSummary({ response }) {
  if (!response) return null;

  return (
    <>
      <h3>Historical Backtest</h3>

      <p>
        <strong>Trades Executed:</strong> {response.backtest.trades}
      </p>

      <p>
        <strong>Winning Trades:</strong> {response.backtest.winning_trades}
      </p>

      <p>
        <strong>Win Rate:</strong> {response.backtest.win_rate}
      </p>

      <p>
        <strong>Total Return:</strong> {response.backtest.total_return}
      </p>

      <p>
        <strong>Max Drawdown:</strong> {response.backtest.max_drawdown}
      </p>

      <hr />
    </>
  );
}

export default BacktestSummary;