function StockTable({ stocks }) {
  return (
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
  );
}

export default StockTable;