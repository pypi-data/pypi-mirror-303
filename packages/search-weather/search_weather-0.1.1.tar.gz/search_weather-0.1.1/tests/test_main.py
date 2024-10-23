import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime
from src.search_weather.main import query, set_api_key, generate_natural_language_response


@pytest.fixture
def mock_query_parser():
    with patch('src.search_weather.main.QueryParser') as MockQueryParser:
        mock_parser = MockQueryParser.return_value
        yield mock_parser


@pytest.fixture
def mock_weather_service():
    with patch('src.search_weather.main.WeatherService') as MockWeatherService:
        mock_service = MockWeatherService.return_value
        yield mock_service


def test_query_with_valid_data(mock_query_parser, mock_weather_service):
    # Mock QueryParser
    mock_query_parser.parse_query.return_value = (datetime.now(), "서울", (37.5665, 126.9780))

    # Mock WeatherService
    mock_weather_service.get_weather.return_value = {
        '날씨': '맑음',
        '최고기온': '25°C',
        '최저기온': '15°C'
    }

    # API 키 설정
    set_api_key('fake_api_key')

    # query 함수 내부에서 사용되는 객체들을 모의 객체로 교체
    with patch('src.search_weather.main.query_parser', mock_query_parser), \
        patch('src.search_weather.main.weather_service', mock_weather_service):

        # WeatherService의 get_weather가 올바르게 호출되었는지 확인
        result = query("내일 서울의 날씨는 어때")

    assert "서울" in result
    assert "맑음" in result
    assert "25°C" in result
    assert "15°C" in result


def test_query_with_invalid_location(mock_query_parser):
    # Mock QueryParser
    mock_query_parser.parse_query.return_value = (datetime.now().date(), None, None)

    result = query("알 수 없는 장소의 날씨는 어때")
    assert result == "위치 정보를 추출할 수 없습니다."


def test_generate_natural_language_response_with_error():
    error_message = "날씨 정보를 가져올 수 없습니다."
    result = generate_natural_language_response("서울", datetime.now(), error_message)
    assert result == error_message
