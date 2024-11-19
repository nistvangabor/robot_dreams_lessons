import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import datetime

# Load API key from secrets
API_KEY = st.secrets["polygon"]["api_key"]

# Base URL for the Polygon API
BASE_URL = "https://api.polygon.io/v2/aggs/ticker"

# Function to fetch stock data
@st.cache_data(ttl=86400)  # Cache results for 24 hours (86400 seconds)
def fetch_stock_data(symbol):
    """Fetch historical stock data for the last 30 days from the Polygon API."""
    print(f"Fetching data for {symbol}")
    
    # Dynamically generate the date range (last 30 days)
    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=30)
    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = today.strftime("%Y-%m-%d")
    
    # Construct the URL directly with the date range
    url = f"{BASE_URL}/{symbol}/range/1/day/{start_date_str}/{end_date_str}"
    
    # Prepare the request with API key
    response = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})
    
    # Check for successful response
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch data: {response.status_code} - {response.text}")
        return None

# Function to process and format the data
def process_data(data):
    """Process the raw data into a pandas DataFrame."""
    if "results" in data:
        # Convert response data into DataFrame
        df = pd.DataFrame(data["results"])
        df['timestamp'] = pd.to_datetime(df['t'], unit='ms')  # Convert 't' to timestamp
        df.set_index('timestamp', inplace=True)
        df = df.rename(columns={
            "o": "Open", "h": "High", "l": "Low", "c": "Close", "v": "Volume", "n": "NumOfTransactions"
        })
        df = df.drop(columns=["t", "vw"])
        print(df.head(20))
        df = df.sort_index()
        print(df.head(20))

        # Convert only numeric columns to float
        print(df.dtypes)
        numeric_columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'NumOfTransactions']
        df[numeric_columns] = df[numeric_columns].astype(float)
        print(df.dtypes)
        return df
    else:
        st.error("No data available.")
        return None

# Streamlit app layout
st.title("Stock Market Dashboard")
st.sidebar.header("Configuration")

# Sidebar inputs
stock_symbol = st.sidebar.text_input("Enter Stock Symbol (e.g., AAPL, TSLA, MSFT)", "AAPL")

# Fetch and process data
data = fetch_stock_data(stock_symbol)
if data:
    df = process_data(data)
    if df is not None:
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
