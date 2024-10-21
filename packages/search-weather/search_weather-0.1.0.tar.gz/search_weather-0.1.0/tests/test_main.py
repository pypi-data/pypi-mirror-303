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
    with patch('src.search_weather.main.QueryParser') as mock_query_parser_class, \
         patch('src.search_weather.main.WeatherService') as mock_weather_service_class, \
         patch('src.search_weather.main.ensure_ko_core_news_sm'):

        # Mock QueryParser
        mock_query_parser = MagicMock()
        mock_query_parser.parse_query.return_value = (datetime.now(), "서울", (37.5665, 126.9780))
        mock_query_parser.api_key = 'fake_api_key'
        mock_query_parser_class.return_value = mock_query_parser

        # Mock WeatherService
        mock_weather_service = MagicMock()
        mock_weather_service.get_weather.return_value = {
            '날짜': datetime.now().strftime("%Y-%m-%d"),
            '날씨': '맑음',
            '최고기온': '25°C',
            '최저기온': '15°C'
        }
        mock_weather_service.check_api_key.return_value = None
        mock_weather_service_class.return_value = mock_weather_service

        # API 키 설정
        set_api_key('fake_api_key')

        result = query("내일 서울의 날씨는 어때")

        assert "서울" in result
        assert "맑음" in result
        assert "25°C" in result
        assert "15°C" in result

        # API 키가 설정되었는지 확인
        mock_weather_service.set_api_key.assert_called_once_with('fake_api_key')


def test_query_with_invalid_location(mock_query_parser):
    # Mock QueryParser
    mock_query_parser.parse_query.return_value = (datetime(2023, 10, 10), None, None)

    result = query("알 수 없는 장소의 날씨는 어때")
    assert result == "위치 정보를 추출할 수 없습니다."


def test_generate_natural_language_response_with_error():
    error_message = "날씨 정보를 가져올 수 없습니다."
    result = generate_natural_language_response("서울", datetime(2023, 10, 10), error_message)
    assert result == error_message
