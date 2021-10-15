import requests
import pprint
import math

api_key = "0a7c75346e71e50eb2513348a463f228"


zip_code = 20020



def get_weather(zip, key):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={zip},us&appid={key}")
    report = response.json()


    city = report['name']
    temp = report['main']['temp']
    feels = report['main']['feels_like']


    temp_f = (float(temp) - 273.15) * 9/5 + 32
    feels_like = (float(feels) - 273.15) * 9/5 + 32


    print(city)
    print(temp_f)
    print(feels_like)


get_weather(zip_code, api_key)

     