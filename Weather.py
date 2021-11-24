import requests
from API import *

apiAddress = "http://api.openweathermap.org/data/2.5/weather?q=Bogra,BD&appid=" + WeatherAPI
Json_Data = requests.get(apiAddress).json()


def temperature():
    temp = round(Json_Data["main"]["temp"] - 273, 1)
    return temp


def description():
    des = Json_Data["weather"][0]["description"]
    return des


# print(temperature())
# print(description())
