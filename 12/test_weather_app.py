# test_weather.py
import pytest
from unittest.mock import MagicMock

from weather_app import WeatherService, WeatherApp


@pytest.fixture
def weather_service_mock():
    # Create a mock for the WeatherService
    #When you set spec=WeatherService, the mock object (mock_service) will only allow calls
    # to methods and access to attributes that exist on WeatherService.
    # This helps ensure that your tests are consistent with the actual class definition and helps catch errors early.
    mock_service = MagicMock(spec=WeatherService)
    mock_service.get_temperature.return_value = 25.0  # Mock temperature
    return mock_service

@pytest.fixture
def weather_app(weather_service_mock):
    # Create an instance of WeatherApp with the mocked service
    return WeatherApp(weather_service_mock)

def test_show_temperature(weather_app, weather_service_mock):
    # Call the method we want to test
    result = weather_app.show_temperature("London")

    # Assert the expected result
    assert result == "The temperature in London is 25.0°C."

    # Verify that the get_temperature method was called once with the correct argument
    weather_service_mock.get_temperature.assert_called_once_with("London")