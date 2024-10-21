# Search Weather

## 목적

Search Weather는 사용자의 자연어 쿼리를 기반으로 날씨 정보를 검색하고 제공하는 파이썬 패키지입니다. 이 프로젝트의 주요 목적은 다음과 같습니다:

1. 사용자가 일상적인 언어로 날씨 정보를 요청할 수 있게 합니다.
2. 위치와 날짜 정보를 자동으로 추출하여 정확한 날씨 정보를 제공합니다.
3. OpenWeatherMap API를 활용하여 신뢰할 수 있는 날씨 데이터를 제공합니다.
4. 날씨 정보를 이해하기 쉬운 자연어 형태로 변환하여 제공합니다.

## 사용하기

### 설치

pip를 사용하여 설치:

```bash
pip install search-weather
```

또는 poetry를 사용하여 설치:

```bash
poetry add search-weather
```

### 기본 사용법

```python
from search_weather import set_api_key, query

# OpenWeatherMap API 키 설정
set_api_key("your_api_key_here")

# 날씨 쿼리 실행
result = query("내일 서울의 날씨는 어때")
print(result)
```

### 주의사항

- OpenWeatherMap API 키가 필요합니다. [OpenWeatherMap](https://openweathermap.org/)에서 무료로 API 키를 발급받을 수 있습니다.
- 처음 사용 시 한국어 언어 모델(ko_core_news_sm)을 자동으로 다운로드합니다. 인터넷 연결이 필요하며 다운로드에 시간이 걸릴 수 있습니다.

## 테스트하기

이 프로젝트는 pytest를 사용하여 테스트를 실행합니다. 테스트를 실행하려면 다음 단계를 따르세요:

1. 프로젝트 루트 디렉토리로 이동합니다.
2. 필요한 의존성을 설치합니다: `pip install -r requirements-dev.txt`
3. 다음 명령어로 테스트를 실행합니다: `pytest tests/`

주요 테스트 케이스:
- API 키 설정 및 조회 테스트
- 쿼리 파싱 테스트
- 위치 정보 변환 테스트
- 날씨 정보 조회 테스트
- 전체 프로세스 테스트
- 에러 처리 테스트

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 연락처

프로젝트 관리자: [minarae](mailto:minarae@gmail.com)

프로젝트 홈페이지: [https://github.com/minarae/search_weather](https://github.com/minarae/search_weather)