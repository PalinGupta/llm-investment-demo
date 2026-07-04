import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [backend, setBackend] = useState("Checking backend...");

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/")
      .then((response) => {
        setBackend(
          `${response.data.project} — ${response.data.status}`
        );
      })
      .catch(() => {
        setBackend("❌ Backend Not Connected");
      });
  }, []);

  return (
    <div
      style={{
        fontFamily: "Arial",
        padding: "40px",
        textAlign: "center",
      }}
    >
      <h1>LLM Investment Strategy Platform</h1>

      <h2>{backend}</h2>

      <p>Frontend and Backend are now connected.</p>
    </div>
  );
}

export default App;