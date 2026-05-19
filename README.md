# 🚀 End-to-End MLOps Stock Prediction Pipeline

An end-to-end AI/ML MLOps project using:

- MLflow
- FastAPI
- Docker
- Prometheus Monitoring
- CI/CD with GitHub Actions
- Logging
- Pytest Testing

This project predicts stock closing prices using machine learning and exposes predictions through a FastAPI REST API.

---

# 📌 Features

✅ Machine Learning Model Training  
✅ MLflow Experiment Tracking  
✅ FastAPI REST API  
✅ Docker Containerization  
✅ Logging System  
✅ Monitoring with Prometheus  
✅ Automated Testing using Pytest  
✅ CI/CD Pipeline using GitHub Actions  

---

# 🏗️ Project Architecture

```text
Dataset
   ↓
Training Pipeline
   ↓
MLflow Tracking
   ↓
Model Saving
   ↓
FastAPI API
   ↓
Docker Container
   ↓
CI/CD Pipeline
   ↓
Monitoring
```

---

# 📂 Project Structure

```text
mlops-stock-prediction/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── api/
│   └── app.py
│
├── data/
│   └── stock.csv
│
├── logs/
│   └── app.log
│
├── models/
│   └── model.pkl
│
├── monitoring/
│   └── metrics.py
│
├── src/
│   ├── train.py
│   ├── predict.py
│   ├── preprocessing.py
│   └── logger.py
│
├── tests/
│   └── test_api.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── mlruns/
```

---

# ⚙️ Installation

## 1 Clone Repository

```bash
git clone https://github.com/your-username/mlops-stock-prediction.git

cd mlops-stock-prediction
```

---

## 2 Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## 3 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📊 Dataset

Use stock dataset with columns:

```text
Open
High
Low
Volume
Close
```

You can download datasets from:

- Kaggle
- Yahoo Finance

---

# 🤖 Train Model

Run:

```bash
python src/train.py
```

This will:

- train the ML model
- save model in `models/`
- log experiments using MLflow

---

# 🔥 MLflow UI

Run:

```bash
mlflow ui
```

Open:

```text
http://127.0.0.1:5000
```

Track:

- parameters
- metrics
- artifacts
- experiments

---

# 🚀 Run FastAPI Server

Run:

```bash
uvicorn api.app:app --reload
```

Open Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# 📦 Docker Setup

Build Docker Image:

```bash
docker build -t stock-mlops .
```

Run Container:

```bash
docker run -p 8000:8000 stock-mlops
```

---

# 🐳 Docker Compose

Run:

```bash
docker-compose up --build
```

---

# 📈 API Example

## POST `/predict`

### Request

```json
{
  "Open": 120,
  "High": 130,
  "Low": 118,
  "Volume": 500000
}
```

### Response

```json
{
  "prediction": 128.45
}
```

---

# 🧪 Run Tests

Run all tests:

```bash
pytest
```

OR

```bash
pytest tests/test_api.py
```

---

# 📋 Logging

Logs are stored in:

```text
logs/app.log
```

Example:

```text
2026-05-19 10:00:00 - INFO - Training Started
```

---

# 📊 Monitoring

Monitoring implemented using:

- Prometheus

Tracks:

- API request count
- API usage

Run monitoring:

```bash
python monitoring/metrics.py
```

---

# 🔄 CI/CD Pipeline

GitHub Actions automatically:

- installs dependencies
- runs tests
- validates code

Workflow file:

```text
.github/workflows/ci.yml
```

---

# 🛠️ Tech Stack

| Tool | Purpose |
|------|----------|
| Python | Programming Language |
| Scikit-learn | Machine Learning |
| MLflow | Experiment Tracking |
| FastAPI | API Framework |
| Docker | Containerization |
| Prometheus | Monitoring |
| Pytest | Testing |
| GitHub Actions | CI/CD |

---

# 🎯 Future Improvements

- Kubernetes Deployment
- AWS Deployment
- DVC Integration
- Airflow Pipeline
- Model Retraining Automation
- Grafana Dashboard

---

# 👨‍💻 Author

Ajit Rout

AI/ML Engineer | MLOps Enthusiast
