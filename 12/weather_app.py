class WeatherService:
    def get_temperature(self, city: str) -> float:
        # Simulates an external API call to get the temperature for a city
        # In reality, this would involve network calls which we want to avoid in unit tests
        raise NotImplementedError("This method should call an external API.")
    

class WeatherApp:
    def __init__(self, service: WeatherService):
        self.service = service

    def show_temperature(self, city: str) -> str:
        temperature = self.service.get_temperature(city)
        return f"The temperature in {city} is {temperature}°C."
    
w_s = WeatherService()
w_a = WeatherApp(service=w_s)

