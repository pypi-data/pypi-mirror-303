import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime
from src.search_weather.get_weather import WeatherService

@pytest.fixture
def weather_service():
    return WeatherService()

@patch('src.search_weather.get_weather.requests.get')
def test_get_weather_with_valid_response(mock_get, weather_service):
    # Mock API response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "list": [
            {
                "dt": datetime.now().timestamp(),
                "main": {"temp_max": 25, "temp_min": 15},
                "weather": [{"description": "맑음"}]
            }
        ]
    }
    mock_get.return_value = mock_response

    weather_service.set_api_key("test_api_key")
    result = weather_service.get_weather(37.5665, 126.9780, datetime.now().date())

    assert result == {
        "날짜": datetime.now().date().strftime("%Y-%m-%d"),
        "날씨": "맑음",
        "최고기온": "25.0°C",
        "최저기온": "15.0°C"
    }


@patch('src.search_weather.get_weather.requests.get')
def test_get_weather_with_invalid_api_key(mock_get, weather_service):
    weather_service.set_api_key(None)
    result = weather_service.get_weather(37.5665, 126.9780, datetime.now().date())
    assert result == "API 키가 설정되지 않았습니다. 'set_api_key' 메서드를 사용하여 API 키를 설정해주세요."

@patch('src.search_weather.get_weather.requests.get')
def test_get_weather_with_failed_response(mock_get, weather_service):
    # Mock failed API response
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    weather_service.set_api_key("test_api_key")
    result = weather_service.get_weather(37.5665, 126.9780, datetime.now().date())
    assert result == "날씨 정보를 가져오는데 실패했습니다."

@patch('src.search_weather.get_weather.requests.get')
def test_get_weather_with_no_data_for_date(mock_get, weather_service):
    # Mock API response with no data for the target date
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"list": []}
    mock_get.return_value = mock_response

    weather_service.set_api_key("test_api_key")
    result = weather_service.get_weather(37.5665, 126.9780, datetime.now().date())
    assert result == "해당 날짜의 날씨 정보를 찾을 수 없습니다."
