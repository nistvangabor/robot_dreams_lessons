import streamlit as st
import time

@st.cache_data(ttl=60) #cache is global for every single user for every single session
def fetch_data(stock_symbol):
    print(stock_symbol)
    time.sleep(3)
    return {"data": "This is cached data"}

st.write("Fetching data...")

stock_symbol = st.sidebar.text_input("Enter Stock Symbol (e.g., AAPL, TSLA, MSFT)", "AAPL")
data = fetch_data(stock_symbol)
st.write(data)
