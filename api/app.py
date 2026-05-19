from fastapi import FastAPI
from fastapi.responses import Response
from pydantic import BaseModel
import joblib
import pandas as pd
from prometheus_client import Counter, generate_latest

app = FastAPI()

# Monitoring Mertic
request_count = Counter(
    "api_requests_total",
    "Total API Requests"
)

model = joblib.load("models/model.pkl")

class StockInput(BaseModel):
    Open: float
    High: float
    Low: float
    Volume: float

@app.get("/")
def home():
    return {"message": "stock Prediction API Running"}


@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type="text/plan"

    )

@app.post("/predict")
def predict(data: StockInput):
    request_count.inc()

    input_data = pd.DataFrame([{
        "Open": data.Open,
        "High": data.High,
        "Low": data.Low,
        "Volume": data.Volume
    }])

    prediction = model.predict(input_data)[0]
    return {
        "prediction": float(prediction)
    }

