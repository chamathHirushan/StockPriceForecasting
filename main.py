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


stocks = ("AAPL", "GOOG", "MSFT", "TSLA", "META")
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


def plot_raw_data(stock_name):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'],
                  y=data['Open'], name=stock_name+" stock open"))
    fig.add_trace(go.Scatter(x=data['Date'],
                  y=data['Close'], name=stock_name+" Stock close"))
    fig.layout.update(title_text='Time Series Data for ' + stock_name,
                      xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)


plot_raw_data(selected_stock)

# Forecasting with prophet
df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": 'ds',
                                    "Close": 'y'})

model = Prophet()
model.fit(df_train)
future = model.make_future_dataframe(periods=period)
forecast = model.predict(future)

# prediction
st.subheader("Forecast data for "+selected_stock)
st.write(forecast.tail())

# plot the prediction
st.write('Forecast'+selected_stock+' data')
fig1 = plot_plotly(model, forecast)
st.plotly_chart(fig1)

st.write('Forecast components of '+selected_stock)
fig2 = model.plot_components(forecast)
st.write(fig2)
