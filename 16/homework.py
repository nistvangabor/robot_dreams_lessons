import streamlit as st
import requests
import pandas as pd

# Function to get current weather data
@st.cache_data(ttl=60)
def get_weather_data(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

# Function to get 5-day forecast data
@st.cache_data(ttl=60)
def get_5day_forecast(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

# Streamlit layout
st.title("Robot Dreams Python - Weather Map & Data Visualization App")

# API Key (Replace with your own API Key)
api_key = st.secrets["weather"]["api_key"]

# City input by the user
city = st.text_input("Enter city name", "London")

if city:
    # Fetch current weather data
    weather_data = get_weather_data(city, api_key)

    # Check if city is found
    if weather_data['cod'] == 200:
        lat = weather_data['coord']['lat']
        lon = weather_data['coord']['lon']
        city_name = weather_data['name']

        # Fetch 5-day forecast data
        forecast_data = get_5day_forecast(city, api_key)

        # Check if forecast data is valid
        if forecast_data['cod'] == '200':
            # Extract necessary weather details
            weather_info = {
                'temp': weather_data['main']['temp'],
                'humidity': weather_data['main']['humidity'],
                'wind_speed': weather_data['wind']['speed'],
            }

            print(weather_info)

            # Display current weather information in separate columns
            st.subheader(f"Current Weather in {city_name}")
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Temperature (°C)", f"{weather_info['temp']}°C")
            with col2:
                st.metric("Humidity (%)", f"{weather_info['humidity']}%")
            with col3:
                st.metric("Wind Speed (m/s)", f"{weather_info['wind_speed']} m/s")

            # Display weather map with city location
            st.subheader("Weather Map")
            location_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})
            st.map(location_data)

            # Process forecast data
            forecast_list = forecast_data['list']
            for x in forecast_list:
                print("------")
                print(x)
            forecast_df = pd.DataFrame({
                'Datetime': [pd.to_datetime(item['dt'], unit='s') for item in forecast_list],
                'Temperature (°C)': [item['main']['temp'] for item in forecast_list],
                'Humidity (%)': [item['main']['humidity'] for item in forecast_list],
                'Wind Speed (m/s)': [item['wind']['speed'] for item in forecast_list]
            })
            forecast_df.set_index('Datetime', inplace=True)

            # Visualization of temperature trends
            st.subheader("Temperature Trends (Next 5 Days)")
            st.line_chart(forecast_df['Temperature (°C)'])

            # Visualization of humidity trends
            st.subheader("Humidity Trends (Next 5 Days)")
            st.line_chart(forecast_df['Humidity (%)'])

            # Visualization of wind speed trends
            st.subheader("Wind Speed Trends (Next 5 Days)")
            st.bar_chart(forecast_df['Wind Speed (m/s)'])

        else:
            st.error("Could not fetch 5-day forecast data. Please try again later.")
    else:
        st.error(f"City {city} not found. Please try another one.")
