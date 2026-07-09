function DashboardCards({ response }) {
  if (!response) return null;

  return (
    <div className="metrics">
      <div className="metric-box">
        <h2>{response.action}</h2>
        <p>Action</p>
      </div>

      <div className="metric-box">
        <h2>{response.stock}</h2>
        <p>Stock</p>
      </div>

      <div className="metric-box">
        <h2>₹{response.current_price}</h2>
        <p>Current Price</p>
      </div>

      <div className="metric-box">
        <h2>{response.signal.includes("Generated") ? "✅" : "❌"}</h2>
        <p>Signal</p>
      </div>
    </div>
  );
}

export default DashboardCards;