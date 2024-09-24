from plotly import graph_objs as go
# Changed from fbprophet.plot to prophet.plot
from prophet.plot import plot_plotly
from prophet import Prophet  # Changed from fbprophet to prophet
import yfinance as yf
from datetime import date
import streamlit as st


START = "2018-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Stock Prediction App")

stocks = ("AAPL", "GOOG", "MSFT")
selected_stock = st.selectbox("Select the dataset for predictions", stocks)

n_years = st.slider("Years of prediction :", 1, 4)

period = n_years * 365


@st.cache_data  # cache the data
def load_data(stock_name):
    data = yf.download(stock_name, START, TODAY)
    data.reset_index(inplace=True)
    return data


data_load_state = st.text("Load data for " + selected_stock + "...")
data = load_data(selected_stock)
data_load_state = st.text("loaded " + selected_stock + " successfully")

st.subheader("Raw data")
st.write(data.tail())
