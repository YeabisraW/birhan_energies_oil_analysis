from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import json

app = Flask(__name__)
CORS(app)

# Load Brent prices
prices = pd.read_csv("dashboard/backend/data/BrentOilPrices.csv")
prices['Date'] = pd.to_datetime(prices['Date']).dt.strftime('%Y-%m-%d')

# Load change points
with open("dashboard/backend/data/change_points.json") as f:
    change_points = json.load(f)


# Load events
# Load events
events = pd.read_csv("dashboard/backend/data/oil_events.csv")
events['Date'] = pd.to_datetime(events['Date']).dt.strftime('%Y-%m-%d')


# Routes
@app.route("/api/prices")
def get_prices():
    return jsonify(prices.to_dict(orient="records"))

@app.route("/api/change-points")
def get_change_points():
    return jsonify(change_points)

@app.route("/api/events")
def get_events():
    return jsonify(events.to_dict(orient="records"))

if __name__ == "__main__":
    print("--- BIRHAN ENERGIES BACKEND LIVE ON PORT 5000 ---")
    app.run(debug=True)
