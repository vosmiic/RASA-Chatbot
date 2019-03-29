import requests
from .getWeather import getLocationWeather, getRainChance

response = requests.get('https://ipinfo.io').json()

def getIPWeather():
    if response['city'] is not '':
        return getLocationWeather(response['city'])
    elif response['region'] is not '':
        return getLocationWeather(response['region'])
    elif response['country'] is not '':
        return getLocationWeather(response['country'])


def getIPWeatherRain():
    if response['city'] is not '':
        return getRainChance(response['city'])
    elif response['region'] is not '':
        return getRainChance(response['region'])
    elif response['country'] is not '':
        return getRainChance(response['country'])
