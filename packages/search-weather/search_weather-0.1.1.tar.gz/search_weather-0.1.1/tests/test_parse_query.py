import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
from src.search_weather.parse_query import QueryParser
from math import floor

@pytest.fixture
def query_parser():
    return QueryParser()

@patch('src.search_weather.parse_query.spacy.load')
@patch('src.search_weather.parse_query.Nominatim')
def test_parse_query_with_valid_data(mock_nominatim, mock_spacy_load, query_parser):
    # Mock spaCy NLP pipeline
    mock_nlp = MagicMock()
    mock_doc = MagicMock()
    mock_doc.ents = [MagicMock(label_='LC', text='서울'), MagicMock(label_='DT', text='내일')]
    mock_nlp.return_value = mock_doc
    mock_spacy_load.return_value = mock_nlp

    # Mock Nominatim geolocator
    mock_geolocator = mock_nominatim.return_value
    mock_geolocator.geocode.return_value = MagicMock(latitude=37.5665, longitude=126.9780)

    date, raw_location, location = query_parser.parse_query("내일 서울의 날씨는 어때")
    assert date == datetime.combine(datetime.now().date() + timedelta(days=1), datetime.min.time())
    assert raw_location == "서울" or raw_location == "서울의"
    assert [int(float(item)) for item in location] == [37, 127]

@patch('src.search_weather.parse_query.spacy.load')
def test_parse_query_with_invalid_location(mock_spacy_load, query_parser):
    # Mock spaCy NLP pipeline
    mock_nlp = MagicMock()
    mock_doc = MagicMock()
    mock_doc.ents = [MagicMock(label_='DT', text='내일')]
    mock_nlp.return_value = mock_doc
    mock_spacy_load.return_value = mock_nlp

    date, raw_location, location = query_parser.parse_query("내일 알 수 없는 장소의 날씨는 어때")
    assert date == datetime.combine(datetime.now().date() + timedelta(days=1), datetime.min.time())
    assert raw_location is None
    assert location is None

@patch('src.search_weather.parse_query.spacy.load')
def test_parse_query_with_invalid_date(mock_spacy_load, query_parser):
    # Mock spaCy NLP pipeline
    mock_nlp = MagicMock()
    mock_doc = MagicMock()
    mock_doc.ents = [MagicMock(label_='LC', text='서울')]
    mock_nlp.return_value = mock_doc
    mock_spacy_load.return_value = mock_nlp

    date, raw_location, location = query_parser.parse_query("알 수 없는 날짜의 서울 날씨는 어때")
    assert date is None
    assert raw_location == "서울"
    assert location is not None
