import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor

DATA_PATH = "data/simulated_product_sales.csv"
RANDOM_STATE = 42

def load_and_prepare_data(path):
    df = pd.read_csv(path, parse_dates=["date"])
    df.sort_values(["product_id", "date"], inplace=True)

    df["price_ratio"] = df["price"] / df["base_price"]
    df["competitor_diff"] = df["price"] - df["competitor_price"]

    df["lag_1"] = df.groupby("product_id")["demand"].shift(1)
    df["lag_7"] = df.groupby("product_id")["demand"].shift(7)

    df["rolling_7"] = (
        df.groupby("product_id")["demand"]
        .shift(1)
        .rolling(7)
        .mean()
    )

    return df.dropna()

