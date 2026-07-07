from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import csv
from services.parser import parse_strategy
from services.backtest import run_backtest
from services.llm_parser import parse_with_llm
from services.strategy_normalizer import normalize_strategy
from services.analysis_generator import generate_analysis

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

    try:
        import json
        parsed = json.loads(parse_with_llm(request.strategy))
        print("✅ Parsed using Ollama")

    except Exception as e:
        print("⚠️ Ollama failed:", e)
        print("⚠️ Falling back to rule-based parser")

        parsed = parse_strategy(request.strategy)

    parsed = normalize_strategy(parsed)

    action = parsed["action"]
    stock = parsed["stock"]
    condition = parsed["condition"]

    strategy = f"{action} {stock} {condition}".upper()

    backtest_result = run_backtest(
        action,
        stock,
        strategy
    )
    analysis = generate_analysis(
        strategy,
        backtest_result["backtest"]
    )

    return {
        "action": action,
        "stock": stock,
        "condition": condition,
        "current_price": backtest_result["current_price"],
        "signal": backtest_result["signal"],
        "backtest": backtest_result["backtest"],
        "analysis": analysis,
    }


@app.get("/stocks")
def get_stocks():
    stocks = []

    with open("data/sample_stock_data.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            stocks.append(row)

    return stocks