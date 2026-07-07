import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

function App() {
  const [stocks, setStocks] = useState([]);
  const [strategy, setStrategy] = useState("");
  const [response, setResponse] = useState(null);
  const [history, setHistory] = useState([]);

  const chartData = [
    { month: "Jan", value: 10000 },
    { month: "Feb", value: 10250 },
    { month: "Mar", value: 10100 },
    { month: "Apr", value: 10650 },
    { month: "May", value: 11050 },
    { month: "Jun", value: 11600 },
    { month: "Jul", value: 12140 },
  ];

  const submitStrategy = async () => {
  try {
    const res = await axios.post(
      "http://127.0.0.1:8000/strategy",
      {
        strategy: strategy,
      }
    );

    setResponse(res.data);
    setHistory((prev) => [res.data, ...prev]);
  } catch (error) {
    console.error(error);
    setResponse("Failed to submit strategy.");
  }
};

useEffect(() => {
  axios
    .get("http://127.0.0.1:8000/stocks")
    .then((response) => {
      setStocks(response.data);
    })
    .catch((error) => {
      console.error("Error fetching stock data:", error);
    });
}, []);
  return (
    <div className="container">
      <h1>LLM Investment Strategy</h1>
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

      <button onClick={submitStrategy}>
        Submit Strategy
      </button>

      {response && (
        <div className="analysis-card">
        
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
          
          <h3>Parsed Strategy</h3>

          <p>
            <strong>Action:</strong> {response.action}
          </p>

          <p>
            <strong>Stock:</strong> {response.stock}
          </p>

          <p>
            <strong>Condition:</strong> {response.condition}
          </p>
          <p>
            <strong>Current Price:</strong> ₹{response.current_price}
          </p>

          <p>
            <strong>Signal:</strong> {response.signal}
          </p>
          <hr />

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

        

        <h3>Portfolio Performance</h3>

        <div style={{ width: "100%", height: 300 }}>
          <ResponsiveContainer>
            <LineChart data={chartData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="month" />
              <YAxis />
              <Tooltip />
              <Line
                type="monotone"
                dataKey="value"
                stroke="#2563eb"
                strokeWidth={3}
              />
            </LineChart>
          </ResponsiveContainer>
        </div>

        <hr />

        <h3>🤖 AI Investment Analysis</h3>

        <div className="analysis-card">
          <p style={{ lineHeight: "1.8" }}>
            {response.analysis}
          </p>
        </div>

       </div>
      )}

      <hr />

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

      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>Symbol</th>
            <th>Company</th>
            <th>Price</th>
            <th>Change</th>
          </tr>
        </thead>

        <tbody>
          {stocks.map((stock, index) => (
            <tr key={index}>
              <td>{stock.Symbol}</td>
              <td>{stock.Company}</td>
              <td>{stock.Price}</td>
              <td>{stock.Change}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;