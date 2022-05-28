# musicnweather
날씨n음악 자동으로 날씨 검색해주는 파트 - 현재 본인의 IP를 가져와서 그 지역의 날씨를 검색해요
이하 전체 코드

import requests
import googlemaps
import json
from pyowm import OWM
from pyowm.utils.config import get_default_config

GOOGLE_API_KEY = ''
API_key = ''

url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={GOOGLE_API_KEY}'
data = {
    'considerIp': True, #현 IP로 데이터 추출
}

result = requests.post(url, data) # 해당 API에 요청을 보내며 데이터를 추출

print(result.text)
result2 = json.loads(result.text)

lat = result2["location"]["lat"] # 현재 위치의 위도 추출
lng = result2["location"]["lng"] # 현재 위치의 경도 추출

gmaps = googlemaps.Client(GOOGLE_API_KEY)

config_dict = get_default_config()
config_dict['language'] = 'kr' #언어 설정

owm = OWM(API_key, config_dict)
mgr = owm.weather_manager()
obs = mgr.weather_at_coords(lat, lng)
w = obs.weather

temperature = w.temp["temp"]-273.15
now = round(temperature, 1)

print('현재 날씨 : ', w.detailed_status, f'{now}도 입니다')
