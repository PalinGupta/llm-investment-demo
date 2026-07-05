import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [stocks, setStocks] = useState([]);
  const [strategy, setStrategy] = useState("");
  const [response, setResponse] = useState(null);

  const submitStrategy = async () => {
  try {
    const res = await axios.post(
      "http://127.0.0.1:8000/strategy",
      {
        strategy: strategy,
      }
    );

    setResponse(res.data);
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
    <div style={{ padding: "20px" }}>
      <h1>LLM Investment Strategy Demo</h1>
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
        <div
          style={{
            marginTop: "20px",
            padding: "15px",
            border: "1px solid #ccc",
            borderRadius: "8px",
            width: "400px",
          }}
        >
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