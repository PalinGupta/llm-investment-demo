import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [stocks, setStocks] = useState([]);

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