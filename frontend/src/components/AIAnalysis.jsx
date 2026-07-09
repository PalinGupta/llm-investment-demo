function AIAnalysis({ response }) {
  if (!response || !response.analysis) return null;

  return (
    <>
      <h3>🤖 AI Investment Analysis</h3>

      <div className="analysis-card">
        <p style={{ lineHeight: "1.8" }}>
          {response.analysis}
        </p>
      </div>

      <hr />
    </>
  );
}

export default AIAnalysis;