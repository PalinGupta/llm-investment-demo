function StrategyHistory({ history }) {
  return (
    <>
      <h2>Strategy History</h2>

      {history.length === 0 ? (
        <p>No strategies submitted yet.</p>
      ) : (
        <div>
          {history.map((item, index) => (
            <div
              key={index}
              className="analysis-card"
              style={{ marginBottom: "15px" }}
            >
              <p><strong>Action:</strong> {item.action}</p>
              <p><strong>Stock:</strong> {item.stock}</p>
              <p><strong>Condition:</strong> {item.condition}</p>
              <p><strong>Signal:</strong> {item.signal}</p>
            </div>
          ))}
        </div>
      )}

      <hr />
    </>
  );
}

export default StrategyHistory;