import re
import requests
import pprint
import math

def get_weather(zip, key):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={zip},us&appid={key}")
    report = response.json()

    status = report['cod']

    if status == 404:
        print('Error code 404 please check your zip code')
        return
    # print(report)

    city = report['name']
    temp = report['main']['temp']
    feels = report['main']['feels_like']


    temp_f = (float(temp) - 273.15) * 9/5 + 32
    real_feel = (float(feels) - 273.15) * 9/5 + 32


    print(city)
    print(temp_f)
    print(real_feel)



api_key = "0a7c75346e71e50eb2513348a463f228"
zip_code = input("Please enter your zip code:")

zip_code_val = False


while zip_code_val is False:
    zip_code_val = True

    #testing
    # length is 5
    if len(zip_code) != 5:
        zip_code_val = False
    # if input are digits
    if not zip_code.isdigit():
        zip_code_val = False
    # if numbers are between 00001 – 99950
    else:
        if int(zip_code) < 1 or int(zip_code) > 99950:
            zip_code_val = False

    # if the validation of zip code is false restart loop        
    if zip_code_val is False:
        print("Please enter a valid zip code 00001- 99950")
        zip_code = input("Please enter your zip code:")

get_weather(zip_code, api_key)

     