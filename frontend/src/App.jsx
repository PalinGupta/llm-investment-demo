import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";
import StrategyForm from "./components/StrategyForm";
import DashboardCards from "./components/DashboardCards";
import ParsedStrategy from "./components/ParsedStrategy";
import BacktestSummary from "./components/BacktestSummary";
import HistoricalChart from "./components/HistoricalChart";
import AIAnalysis from "./components/AIAnalysis";
import StrategyHistory from "./components/StrategyHistory";
import StockTable from "./components/StockTable";

function App() {
  const [stocks, setStocks] = useState([]);
  const [strategy, setStrategy] = useState("");
  const [response, setResponse] = useState(null);
  const [history, setHistory] = useState([]);
  const [chartData, setChartData] = useState([]);

  const [loading, setLoading] = useState(false);

  const submitStrategy = async () => {
    setLoading(true);
    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/strategy",
        {
          strategy: strategy,
        }
      );

      setResponse(res.data);
      setHistory((prev) => [res.data, ...prev]);
      
      const historyRes = await axios.get(
        `http://127.0.0.1:8000/history/${res.data.stock}`
      );

      setChartData(historyRes.data);
      setLoading(false);

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
      <StrategyForm
        strategy={strategy}
        setStrategy={setStrategy}
        submitStrategy={submitStrategy}
        loading={loading}

      />

      {response && (
        <div className="analysis-card">
        
          <DashboardCards response={response} />
          
          <ParsedStrategy response={response} />

        <BacktestSummary response={response} />

        

        <HistoricalChart chartData={chartData} />

        <AIAnalysis response={response} />

       </div>
      )}

      <hr />

      <StrategyHistory history={history} />
      

      <hr />

      <StockTable stocks={stocks} />

    </div>
  );
}

export default App;