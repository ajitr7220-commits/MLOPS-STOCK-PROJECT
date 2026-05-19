import pandas as pd
import mlflow
import mlflow.sklearn
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from logger import logger
logger.info("Training started")

#load dataset
df = pd.read_csv("data/stocks/stock.csv")
x = df[["Open", "High", "Low", "Volume"]]
y = df["Close"]

# split data
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

#split Data
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

#Mlflow
mlflow.set_tracking_uri("file:./mlruns")
mlflow.set_experiment("stock Prediction")

with mlflow.start_run():
    model = RandomForestRegressor()
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    rmse = mean_squared_error(y_test, predictions)
     
# Log parameters
mlflow.log_param("model", "RandomForest")

# Log Metrics
mlflow.log_metric('rmse', rmse)

# save model
joblib.dump(model, "models/model.pkl")

mlflow.sklearn.log_model(model, "model")


logger.info(f"RMSE: {rmse}")

print("Training completed")