import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA

# Load data
df = pd.read_csv("Expt-7_time_series_covid19.csv")

# Assuming the time columns start from index 11
date_columns = df.columns[11:]

# Sum up all the columns to get the total number of cases
time_series = df[date_columns].sum(axis=0)

# Convert the index to datetime format
time_series.index = pd.to_datetime(time_series.index)

# Check for missing values
if time_series.isnull().sum() > 0:
    print("Missing values detected! Filling missing values...")
    time_series = time_series.fillna(method='ffill')  # Forward fill missing values

# Plot the time series
def plot_series(series, title="Time Series"):
    plt.figure(figsize=(12, 5))
    plt.plot(series, label="Total Cases")
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Total Cases")
    plt.legend()
    plt.show()

plot_series(time_series, title="COVID-19 Cases Over Time")

# Fit ARIMA model
try:
    model = ARIMA(time_series, order=(1, 1, 1))
    model_fit = model.fit()

    # Print model summary
    print(model_fit.summary())

    # In-sample prediction (fitted values)
    in_sample_preds = model_fit.predict(start=1, end=len(time_series)-1, typ="levels")

    # Forecast the next 30 days
    future_forecast = model_fit.forecast(steps=30)

    # Combine actual, in-sample prediction, and forecast
    def plot_all(series, in_sample, forecast):
        plt.figure(figsize=(14, 6))
        plt.plot(series, label="Actual", color="blue")
        plt.plot(in_sample.index, in_sample, label="In-sample Prediction", color="green")
        future_index = pd.date_range(start=series.index[-1] + pd.Timedelta(days=1), periods=30, freq="D")
        plt.plot(future_index, forecast, label="Forecast (30 days)", color="red")
        plt.title("COVID-19 ARIMA Fit and Forecast")
        plt.xlabel("Date")
        plt.ylabel("Total Cases")
        plt.legend()
        plt.show()

    plot_all(time_series, in_sample_preds, future_forecast)

except Exception as e:
    print(f"Error during ARIMA fitting: {e}")
