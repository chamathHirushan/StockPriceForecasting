from plotly import graph_objs as go
# Changed from fbprophet.plot to prophet.plot
from prophet.plot import plot_plotly
from prophet import Prophet  # Changed from fbprophet to prophet
import yfinance as yf
from datetime import date
import streamlit as st

print("hello world")


START = "2018-01-01"
TODAY = date.today().strtime("%Y-%m-%d")

st.title("Stock Prediction App")

stocks = ("AAPL", "GOOG", "MSFT")
selected_stocks = st.selectbox("Select the dataset for predictions", stocks)

n_years = st.slider("Years of prediction :", 1, 4)

period = n_years * 365
