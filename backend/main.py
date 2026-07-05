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
    return {
        "message": "Strategy received successfully!",
        "strategy": request.strategy
    }

@app.get("/stocks")
def get_stocks():
    stocks = []

    with open("data/sample_stock_data.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            stocks.append(row)

    return stocks