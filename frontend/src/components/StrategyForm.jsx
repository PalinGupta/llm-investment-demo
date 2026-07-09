function StrategyForm({
  strategy,
  setStrategy,
  submitStrategy,
  loading,
}) {
  return (
    <>
      <h2>Enter Investment Strategy</h2>

      <textarea
        rows="4"
        cols="60"
        value={strategy}
        onChange={(e) => setStrategy(e.target.value)}
        placeholder="Example: Buy TCS when price is above 4000"
      />

      <br />
      <br />

      <button
        onClick={submitStrategy}
        disabled={loading}
      >
        {loading ? "Analyzing..." : "Submit Strategy"}
      </button>

      {loading && (
        <p style={{ marginTop: "15px" }}>
          🤖 Parsing strategy...
          <br />
          📈 Running historical backtest...
          <br />
          🧠 Generating AI investment analysis...
        </p>
      )}
    </>
  );
}

export default StrategyForm;    