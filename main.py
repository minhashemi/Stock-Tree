# pricey
# CS50x Final Project
# Amin Hashemi (@minhashemi)
############################

#   required libraries
import sys
# data analyze
import numpy as np

# get data from Yahoo Finance API
import yfinance as yf

# prediction module
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# plot
import matplotlib.pyplot as plt

#   get user data
ticker = (
    input("Enter the ticker (symbol) of company you want to check for predictions: ")
    .strip()
    .upper()
)
#   get stock info
start_date = "2017-12-26"
end_date = "2022-12-26"
df = yf.download(ticker, start=start_date, end=end_date)

df = df[["Close"]]

# how many days to predict
days = 30
df["Prediction"] = df[["Close"]].shift(-days)

X = np.array(df.drop(["Prediction"], 1))[:-days]
y = np.array(df["Prediction"])[:-days]
try:
    x_train, y_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
except ValueError:
    sys.exit("Not enough data! Make sure you use a correct ticker and time period is at least 6 months.")

tree_regression = DecisionTreeRegressor().fit(x_train, y_train)

x_future = df.drop(["Prediction"], 1)[:-days]
x_future = x_future.tail(days)
x_future = np.array(x_future)

tree_prediction = tree_regression.predict(x_future)

#   decision tree prediction
predictions = tree_prediction
valid = df[X.shape[0] :]
valid["Predictions"] = predictions

# plot former and predicted data
plt.style.use("bmh")
plt.figure(figsize=(12, 7))
plt.title("Model with Linear Regression")
plt.xlabel("Days")
plt.ylabel("Close Price ($)")
plt.plot(df["Close"])
plt.plot(valid[["Close", "Predictions"]])
plt.legend(["Orig", "Val", "Pred"])
plt.show()
