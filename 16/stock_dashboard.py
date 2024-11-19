import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import pprint
import datetime
import time
# Load API key from secrets
API_KEY = st.secrets["alphavantage"]["api_key"]
#9YSY0GVMKU8GOUY5
#CPGH9918CCV5A558

# Base URL for the Alpha Vantage API
BASE_URL = "https://www.alphavantage.co/query"

#https://www.alphavantage.co/documentation/

# Function to calculate the number of seconds until midnight
def seconds_until_midnight():
    now = datetime.datetime.now()
    midnight = datetime.datetime.combine(now.date() + datetime.timedelta(days=1), datetime.time(0, 0))
    return (midnight - now).seconds

# Function to fetch stock data
@st.cache_data(ttl=86400)  # Cache results for 24 hours (86400 seconds)
def fetch_stock_data(symbol):
    print(f"function run for {symbol}")
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY,
    }
    response = requests.get(BASE_URL, params=params)
    print(response.headers)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch data from Alpha Vantage: {response.text}.")
        return None

# Streamlit app layout
st.title("Stock Market Dashboard")
st.sidebar.header("Configuration")

# Sidebar inputs
stock_symbol = st.sidebar.text_input("Enter Stock Symbol (e.g., AAPL, TSLA, MSFT)", "AAPL")

# Fetch data
data = fetch_stock_data(stock_symbol)
print(data)
if data and "Time Series (Daily)" in data:
    time_series = data["Time Series (Daily)"]
    print(time_series)
    # Transform data into a DataFrame
    df = pd.DataFrame.from_dict(time_series, orient="index")
    pprint.pprint(df.head(20))
    df = df.rename(
        columns={
            "1. open": "Open",
            "2. high": "High",
            "3. low": "Low",
            "4. close": "Close",
            "5. volume": "Volume",
        }
    )
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    df = df.astype(float)

    # Display KPIs side-by-side
    st.header(f"Stock Overview: {stock_symbol.upper()}")
    kpi1, kpi2, kpi3 = st.columns(3)

    with kpi1:
        st.metric(label="Latest Closing Price", value=f"${df['Close'].iloc[-1]:.2f}")
    with kpi2:
        st.metric(label="Volume", value=f"{df['Volume'].iloc[-1]:,.0f}")
    with kpi3:
        st.metric(label="Highest Price (Last 30 Days)", value=f"${df['High'][-30:].max():.2f}")

        
    # Line chart for closing prices
    st.subheader("Closing Price Over Time")
    fig_close = px.line(df, x=df.index, y="Close", title=f"{stock_symbol.upper()} Closing Price Over Time")
    st.plotly_chart(fig_close)

    # Volume bar chart
    st.subheader("Trading Volume Over Time")
    fig_volume = px.bar(df, x=df.index, y="Volume", title=f"{stock_symbol.upper()} Trading Volume Over Time")
    st.plotly_chart(fig_volume)

    # Raw data
    st.subheader("Raw Data")
    st.write(df)
else:
    st.error("No data available. Check the stock symbol or try again later.")