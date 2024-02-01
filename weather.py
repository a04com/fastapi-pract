import requests

def getParams(city):
    return {
    'key': '804c97b061374c55b9583509240102',
    'q': city,
    'days': "1"
    }
def getWeather(city):
    reponse = requests.get("https://api.weatherapi.com/v1/forecast.json", params=getParams(city))
    return reponse.json()['current']['temp_c']
