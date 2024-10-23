import spacy
from geopy.geocoders import Nominatim
from datetime import datetime, timedelta
from typing import Tuple, Optional, List


class QueryParser:
    def __init__(self):
        self.nlp = spacy.load("ko_core_news_sm")
        self._add_custom_entities()
        self.geolocator = Nominatim(user_agent="search_weather")

    def _add_custom_entities(self):
        # 사용자 정의 엔티티 추가
        ruler = self.nlp.add_pipe("entity_ruler")
        patterns = [
            {"label": "LC", "pattern": "하와이"},
            {"label": "LC", "pattern": "LA"},
            {"label": "LC", "pattern": "뉴욕"},
        ]
        ruler.add_patterns(patterns)

    def parse_query(self, query: str) -> Tuple[Optional[datetime], Optional[str], Optional[List[str]]]:
        """
        쿼리를 파싱하여 날짜와 위치 정보를 추출합니다.
        """
        doc = self.nlp(query)
        date = self._extract_date(query, doc)
        location = self._extract_location(doc)
        raw_location = None
        if location:
            raw_location = location[0]
            location = self._validate_location(location[0])

        return date, raw_location, location

    def _extract_location(self, doc: spacy.tokens.Doc) -> Optional[List[str]]:
        """
        주어진 문서에서 위치 정보를 추출합니다.
        """
        locations = []
        for ent in doc.ents:
            if ent.label_ == "LC":
                locations.append(ent.text)

        if not locations:
            # 엔티티로 인식되지 않은 위치명을 찾습니다.
            location_keywords = ["서울", "부산", "인천", "대구", "광주", "대전", "울산", "세종", "제주"]
            for token in doc:
                if token.text in location_keywords:
                    locations.append(token.text)

        return locations if locations else None

    def _extract_date(self, query: str, doc: spacy.tokens.Doc) -> Optional[datetime]:
        """
        주어진 문서에서 날짜 정보를 추출합니다.
        """
        today = datetime.now().date()
        date_keywords = {
            '오늘': 0,
            '내일': 1,
            '모레': 2,
            '글피': 3,
            '주말': [5, 6],  # 토요일, 일요일
        }

        for ent in doc.ents:
            if ent.label_ == "DT":
                date_text = ent.text
                if date_text == "내일" and "모레" in query:
                    date_text = "모레"

                today = datetime.now().date()

                if "오늘" in date_text:
                    return datetime.combine(today, datetime.min.time())
                elif "내일" in date_text:
                    return datetime.combine(today + timedelta(days=1), datetime.min.time())
                elif "모레" in date_text:
                    return datetime.combine(today + timedelta(days=2), datetime.min.time())
                elif "글피" in date_text:
                    return datetime.combine(today + timedelta(days=3), datetime.min.time())
                elif "주말" in date_text:
                    days_until_saturday = (5 - today.weekday() + 7) % 7
                    return datetime.combine(today + timedelta(days=days_until_saturday), datetime.min.time())

        for token in doc:
            if token.text in date_keywords:
                days = date_keywords[token.text]
                if isinstance(days, list):
                    today = datetime.now()
                    saturday = today + timedelta((5 - today.weekday() + 7) % 7)
                    return saturday
                else:
                    return datetime.now() + timedelta(days=days)

        return None

    def _validate_location(self, location: str) -> Optional[List[str]]:
        """
        주어진 위치를 검증하고 좌표를 반환합니다.
        """
        try:
            location_info = self.geolocator.geocode(location)
            if location_info:
                return [str(location_info.latitude), str(location_info.longitude)]
        except Exception as e:
            print(f"위치 검증 중 오류 발생: {e}")
        return None
