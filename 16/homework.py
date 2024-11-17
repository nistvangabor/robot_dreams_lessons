import streamlit as st
import requests
import pandas as pd

# Function to get weather data from OpenWeatherMap
def get_weather_data(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

# Streamlit layout
st.title("Weather Map & Data Visualization App")

# API Key (Replace with your own API Key)
api_key = st.secrets["weather"]["api_key"]

# City input by the user
city = st.text_input("Enter city name", "London")

if city:
    # Fetch weather data
    weather_data = get_weather_data(city, api_key)

    # Check if city is found
    if weather_data['cod'] == 200:
        lat = weather_data['coord']['lat']
        lon = weather_data['coord']['lon']
        city_name = weather_data['name']
        
        # Extract necessary weather details
        weather_info = {
            'temp': weather_data['main']['temp'],
            'humidity': weather_data['main']['humidity'],
            'wind_speed': weather_data['wind']['speed'],
        }
        
        # Display weather information
        st.subheader(f"Weather in {city_name}")
        st.write(f"Temperature: {weather_info['temp']}°C")
        st.write(f"Humidity: {weather_info['humidity']}%")
        st.write(f"Wind Speed: {weather_info['wind_speed']} m/s")

        # Display weather map with city location
        st.subheader("Weather Map")
        location_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})
        st.map(location_data)  # Streamlit built-in map visualization

        # Display temperature, humidity, and wind speed data using Streamlit's built-in charts
        st.subheader("Weather Data Visualization")

        # Bar chart for temperature, humidity, and wind speed
        weather_df = pd.DataFrame({
            'Metric': ['Temperature (°C)', 'Humidity (%)', 'Wind Speed (m/s)'],
            'Value': [weather_info['temp'], weather_info['humidity'], weather_info['wind_speed']]
        })
        st.bar_chart(weather_df.set_index('Metric'))

        # Line chart for the same metrics (just for demonstration)
        st.line_chart(weather_df.set_index('Metric')['Value'])

    else:
        st.error(f"City {city} not found. Please try another one.")