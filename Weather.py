import requests
import pprint
import math
import re

api_key = "0a7c75346e71e50eb2513348a463f228"
zip_code_val = ("[0-9]{5}")

user_input = input("Please enter your zip code:")

# def validate_user_zip(user_zip, zip_hold):
#     while True:
#         try:
#             user_zip = input("Please enter your zip code:")
#         except ValueError:
#             print('Please enter a valid US based Zip Code, valid format and range are 00001 – 99950')
#         else:
#             print 'Thanks,',x,'is indeed an integer'
#             break

#     if (user_zip == zip_hold):
#         print('Here is your weather report')  
#     else:
#         if (user_zip != zip_hold):
#             print('Please enter a valid US based Zip Code, valid format and range are 00001 – 99950')
#             input("Please enter your zip code:")
        

validate_user_zip(user_input, zip_code_val)

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

     