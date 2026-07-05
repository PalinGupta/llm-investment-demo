from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import csv

app = FastAPI(
    title="LLM Investment Strategy Platform",
    version="0.1"
)

# Allow React frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "project": "LLM Investment Strategy Platform",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

class StrategyRequest(BaseModel):
    strategy: str

@app.post("/strategy")
def submit_strategy(request: StrategyRequest):

    strategy = request.strategy.upper()

    action = "UNKNOWN"
    stock = "UNKNOWN"
    condition = "UNKNOWN"

    # Detect BUY / SELL
    if "BUY" in strategy:
        action = "BUY"
    elif "SELL" in strategy:
        action = "SELL"

    # Detect stock
    stocks = [
        "RELIANCE",
        "TCS",
        "INFY",
        "HDFCBANK",
        "ICICIBANK",
        "SBIN"
    ]

    for s in stocks:
        if s in strategy:
            stock = s
            break

    # Detect condition
    if "ABOVE" in strategy:
        price = strategy.split("ABOVE")[-1].strip()
        condition = f"Price Above {price}"

    elif "BELOW" in strategy:
        price = strategy.split("BELOW")[-1].strip()
        condition = f"Price Below {price}"

    current_price = None

    with open("data/sample_stock_data.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if row["Symbol"] == stock:
                current_price = float(row["Price"])
                break
    
    signal = "No Signal"

    if current_price is not None:

        if "ABOVE" in strategy:
            target_price = float(strategy.split("ABOVE")[-1].strip())

            if current_price > target_price:
                if action == "BUY":
                    signal = "Buy Signal Generated ✅"
                elif action == "SELL":
                    signal = "Sell Signal Generated ✅"

        elif "BELOW" in strategy:
            target_price = float(strategy.split("BELOW")[-1].strip())

            if current_price < target_price:
                if action == "BUY":
                    signal = "Buy Signal Generated ✅"
                elif action == "SELL":
                    signal = "Sell Signal Generated ✅"

    return {
    "action": action,
    "stock": stock,
    "condition": condition,
    "current_price": current_price,
    "signal": signal
}

@app.get("/stocks")
def get_stocks():
    stocks = []

    with open("data/sample_stock_data.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            stocks.append(row)

    return stocks