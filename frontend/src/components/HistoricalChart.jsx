import {
  ResponsiveContainer,
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
} from "recharts";

function HistoricalChart({ chartData }) {
  if (!chartData || chartData.length === 0) return null;

  return (
    <>
      <h3>Portfolio Performance</h3>

      <div style={{ width: "100%", height: 300 }}>
        <ResponsiveContainer>
          <LineChart data={chartData}>
            <CartesianGrid strokeDasharray="3 3" />

            <XAxis
              dataKey="Date"
              hide
            />

            <YAxis />

            <Tooltip />

            <Line
              type="monotone"
              dataKey="Close"
              stroke="#2563eb"
              strokeWidth={2}
              dot={false}
            />
          </LineChart>
        </ResponsiveContainer>
      </div>

      <hr />
    </>
  );
}

export default HistoricalChart;