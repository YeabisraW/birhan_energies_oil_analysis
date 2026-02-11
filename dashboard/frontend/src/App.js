import React, { useEffect, useState } from "react";
import axios from "axios";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
  ReferenceLine,
} from "recharts";

function App() {
  const [prices, setPrices] = useState([]);
  const [changePoints, setChangePoints] = useState([]);
  const [events, setEvents] = useState([]);
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");

  useEffect(() => {
    // Fetch Brent prices
    axios
      .get("http://127.0.0.1:5000/api/prices")
      .then((res) => {
        const formatted = res.data.map((item) => ({
          Date: item.Date,
          Price: Number(item.Price),
        }));
        setPrices(formatted);
      })
      .catch((err) => console.error("Prices API error:", err));

    // Fetch change points
    axios
      .get("http://127.0.0.1:5000/api/change-points")
      .then((res) => setChangePoints(res.data))
      .catch((err) => console.error("Change points API error:", err));

    // Fetch events
    axios
      .get("http://127.0.0.1:5000/api/events")
      .then((res) => setEvents(res.data))
      .catch((err) => console.error("Events API error:", err));
  }, []);

  // Filter prices by date range
  const filteredPrices = prices.filter((p) => {
    const date = new Date(p.Date);
    const afterStart = startDate ? date >= new Date(startDate) : true;
    const beforeEnd = endDate ? date <= new Date(endDate) : true;
    return afterStart && beforeEnd;
  });

  return (
    <div
      style={{
        width: "95%",
        margin: "auto",
        paddingTop: "20px",
        fontFamily: "Arial, sans-serif",
      }}
    >
      <h1 style={{ textAlign: "center", color: "#2c3e50" }}>
        Brent Oil Price Dashboard
      </h1>
      <p style={{ textAlign: "center", color: "#34495e" }}>
        Data loaded: {filteredPrices.length} points
      </p>

      {/* Date range filter */}
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          marginBottom: "20px",
          gap: "20px",
        }}
      >
        <div>
          <label style={{ fontWeight: "bold", marginRight: "5px" }}>
            Start Date:
          </label>
          <input
            type="date"
            value={startDate}
            onChange={(e) => setStartDate(e.target.value)}
            style={{ padding: "5px", borderRadius: "4px" }}
          />
        </div>
        <div>
          <label style={{ fontWeight: "bold", marginRight: "5px" }}>
            End Date:
          </label>
          <input
            type="date"
            value={endDate}
            onChange={(e) => setEndDate(e.target.value)}
            style={{ padding: "5px", borderRadius: "4px" }}
          />
        </div>
      </div>

      {filteredPrices.length > 0 && (
        <ResponsiveContainer width="100%" height={500}>
          <LineChart data={filteredPrices}>
            <CartesianGrid strokeDasharray="3 3" stroke="#ecf0f1" />
            <XAxis
              dataKey="Date"
              tickFormatter={(tick) => tick.slice(0, 7)}
              angle={-45}
              textAnchor="end"
              interval="preserveStartEnd"
              height={70}
              stroke="#34495e"
            />
            <YAxis
              domain={["auto", "auto"]}
              stroke="#34495e"
              tickFormatter={(value) => `$${value}`}
            />
            <Tooltip
              labelFormatter={(label) => `Date: ${label}`}
              formatter={(value, name) => [`$${value}`, "Price"]}
              contentStyle={{ backgroundColor: "#f0f3f7", borderRadius: "5px" }}
            />

            {/* Brent Price Line */}
            <Line
              type="monotone"
              dataKey="Price"
              stroke="#2980b9"
              dot={false}
              strokeWidth={2}
            />

            {/* Change Points */}
            {changePoints.map((cp, index) => (
              <ReferenceLine
                key={index}
                x={cp.date}
                stroke="red"
                strokeWidth={2}
                label={{
                  value: "Change Point",
                  position: "top",
                  fill: "red",
                  fontSize: 12,
                }}
              />
            ))}

            {/* Events */}
            {events.map((event, index) => (
              <ReferenceLine
                key={index}
                x={event.date}
                stroke="green"
                strokeWidth={2}
                label={{
                  value: event.event,
                  position: "top",
                  fill: "green",
                  fontSize: 12,
                  angle: -45,
                }}
              />
            ))}
          </LineChart>
        </ResponsiveContainer>
      )}
    </div>
  );
}

export default App;
