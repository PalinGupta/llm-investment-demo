function ParsedStrategy({ response }) {
  if (!response) return null;

  return (
    <>
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
    </>
  );
}

export default ParsedStrategy;