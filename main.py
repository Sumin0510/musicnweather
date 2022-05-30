import requests
import googlemaps
import json
from pyowm import OWM
from pyowm.utils.config import get_default_config


GOOGLE_API_KEY = 'AIzaSyCKqc__yNSlC-9IspRAZWxU7GskBv6-z-8'
API_key = '27c674b1ce585ff4aea4fc73ac8b3d32'

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

wlist = ['맑음', '흐림', '비', '눈']

if w.detailed_status in wlist:
    print("현재 날씨 : ", w.detailed_status)

else:
    if '맑음' in w.detailed_status:
        print("현재 날씨 : 맑음")

    elif '흐림' in w.detailed_status:
        print("현재 날씨 : 흐림")

    elif '비' in w.detailed_status:
        print("현재 날씨 : 비")

    elif '눈' in w.detailed_status:
        print("현재 날씨 : 눈")

    else:
        print("날씨에 따른 추천 음악 리스트를 찾을 수 없습니다")
