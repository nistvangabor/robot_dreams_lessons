import requests
import weather_settings as ws

#
#https://openweathermap.org/current
# Define base URL and parameters
url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "lat": ws.BUDAPEST.get("lat", 0),
    "lon": ws.BUDAPEST.get("lon", 0),
    "appid": ws.WEATHERMAP_API_KEY,  
    "units": "metric"
}

try:
    # Send GET request
    response = requests.get(url, params=params)
    response.raise_for_status()  # Check for HTTP errors (raises exception for 4xx and 5xx codes)

    # Try to parse JSON response
    weather_data = response.json()
    print(type(weather_data))
    # Extracting data
    city = weather_data.get("name", "Unknown location")
    temp = weather_data["main"].get("temp", "N/A")
    weather_desc = weather_data["weather"][0].get("description", "No description available")
    
    # Print weather information
    print(f"City: {city}")
    print(f"Temperature: {temp}°C")
    print(f"Weather Description: {weather_desc}")

# Handle HTTP errors (e.g., 404 Not Found, 401 Unauthorized)
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err} - {response.json().get('message', 'No details')}")
    
# Handle network-related errors (e.g., DNS failure, refused connection)
except requests.exceptions.ConnectionError as conn_err:
    print(f"Network error occurred: {conn_err}")

# Handle invalid JSON response or other parsing errors
except ValueError as json_err:
    print(f"Error parsing JSON response: {json_err}")

# Handle other possible exceptions (optional, catch-all)
except Exception as err:
    print(f"An unexpected error occurred: {err}")