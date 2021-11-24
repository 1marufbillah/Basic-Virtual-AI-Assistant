import requests
from API import *

apiAddress = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + NewsAPI
json_Data = requests.get(apiAddress).json()

ar = []


def news():
    for i in range(3):
        ar.append("Headline " + str(i + 1) + ", " + json_Data["articles"][i]["title"] + ".")

    return ar

# array = news()
# print(array)
