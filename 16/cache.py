import streamlit as st
import time

@st.cache_data(ttl=60) #cache is global for every single user for every single session
def fetch_data():
    time.sleep(3)
    return {"data": "This is cached data"}

st.write("Fetching data...")
data = fetch_data()
st.write(data)