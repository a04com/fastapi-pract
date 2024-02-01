import requests
import json

def getParams(city):
    return {
    'key': '804c97b061374c55b9583509240102',
    'q': city,
    'days': "1"
    }
def getWeather(city):
    jsonDict = {}
    response = requests.get("https://api.weatherapi.com/v1/forecast.json", params=getParams(city)).json()['current']
    jsonDict['Temperature celsius'] = response['temp_c']
    jsonDict['Temperature fahrenheit'] = response['temp_f']
    jsonDict['Last update'] = response['last_updated']

    return jsonDict
