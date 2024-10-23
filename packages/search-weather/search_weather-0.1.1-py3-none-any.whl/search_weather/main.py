from search_weather.get_weather import WeatherService
from search_weather.parse_query import QueryParser
import random
from datetime import timedelta
import spacy
import subprocess

query_parser = QueryParser()
weather_service = WeatherService()


def ensure_ko_core_news_sm():
    """한국어 모델이 설치되어 있는지 확인하고, 없으면 설치"""
    try:
        spacy.load("ko_core_news_sm")
    except OSError:
        subprocess.check_call(["python", "-m", "spacy", "download", "ko_core_news_sm"])


def generate_natural_language_response(location, date, weather_info):
    """날씨 정보를 자연스러운 한국어 문장으로 변환"""
    if isinstance(weather_info, str):
        return weather_info  # 에러 메시지 그대로 반환

    # 날짜 표현 변환
    date_str = date.strftime("%Y년 %m월 %d일")
    today = date.today()
    if date == today:
        date_expr = "오늘"
    elif date == today + timedelta(days=1):
        date_expr = "내일"
    elif date == today + timedelta(days=2):
        date_expr = "모레"
    else:
        date_expr = date_str

    # 날씨 설명에 따른 추가 표현
    weather_expr = {
        "맑음": ["화창한", "좋은", "멋진"],
        "흐림": ["흐린", "꾸물꾸물한", "우중충한"],
        "비": ["비가 오는", "우산이 필요한", "축축한"],
        "눈": ["눈이 오는", "하얀", "로맨틱한"],
        "구름": ["구름 낀", "선선한", "산책하기 좋은"]
    }

    weather = weather_info['날씨']
    temp_max = weather_info['최고기온']
    temp_min = weather_info['최저기온']

    # 기본 템플릿 문장
    templates = [
        "{date_expr} {location}의 날씨는 {weather}입니다. 최고기온은 {temp_max}, 최저기온은 {temp_min}로 예상됩니다.",
        "{location}의 {date_expr} 날씨를 알려드릴게요. {weather}이(가) 예상되며, 기온은 {temp_min}에서 {temp_max} 사이가 될 것 같아요.",
        "{date_expr} {location} 지역은 {weather} 날씨가 예보되고 있어요. 기온은 최저 {temp_min}, 최고 {temp_max}가 될 거예요."
    ]

    # 날씨에 따른 추가 코멘트
    weather_comments = {
        "맑음": [
            "날씨가 좋으니 야외 활동하기 좋은 날이에요!",
            "화창한 날씨를 즐기기 좋겠어요.",
            "맑은 하늘을 구경하기 좋은 날이에요."
        ],
        "흐림": [
            "우산을 챙기시는 게 좋을 것 같아요.",
            "실내 활동을 계획해보는 건 어떨까요?",
            "날씨가 꾸물꾸물하네요."
        ],
        "비": [
            "우산 꼭 챙기세요!",
            "비 오는 날의 운치를 즐겨보는 것도 좋겠어요.",
            "실내에서 따뜻한 차 한 잔 어떠세요?"
        ],
        "눈": [
            "로맨틱한 눈 구경 어떠세요?",
            "미끄러우니 조심히 다니세요.",
            "눈사람 만들기 좋은 날이에요!"
        ],
        "구름": [
            "구름 낀 하늘도 나름의 매력이 있어요.",
            "선선한 날씨를 즐겨보세요.",
            "산책하기 좋은 날씨에요."
        ]
    }

    # 날씨 키워드 추출
    weather_key = next((key for key in weather_expr.keys() if key in weather), "기타")

    # 템플릿 선택 및 형식화
    response = random.choice(templates).format(
        date_expr=date_expr,
        location=location,
        weather=weather,
        temp_max=temp_max,
        temp_min=temp_min
    )

    # 날씨 표현 추가
    if weather_key in weather_expr:
        response = response.replace(weather, random.choice(weather_expr[weather_key]) + " " + weather)

    # 날씨 코멘트 추가
    if weather_key in weather_comments:
        response += " " + random.choice(weather_comments[weather_key])

    return response


def set_api_key(api_key):
    """WeatherService에 API 키를 설정"""
    global weather_service
    weather_service.set_api_key(api_key)


def query(query):
    """사용자의 쿼리를 처리하고 날씨 정보를 반환"""
    ensure_ko_core_news_sm()
    date, raw_location, location = query_parser.parse_query(query)
    if location and date:
        latitude, longitude = location
        weather_info = weather_service.get_weather(latitude, longitude, date.date())
        if isinstance(weather_info, dict):
            return generate_natural_language_response(raw_location, date, weather_info)
        else:
            return weather_info
    elif location is None:
        return "위치 정보를 추출할 수 없습니다."
    else:
        return "날짜 정보를 추출할 수 없습니다."
