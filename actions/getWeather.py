import pywapi

def getLocationWeather(sentLocation):
    location = pywapi.get_location_ids(sentLocation)
    weather_result = pywapi.get_weather_from_weather_com(next(iter(location)))
    conditions = str(weather_result['current_conditions']['text'])
    temperature = str(weather_result['current_conditions']['temperature'])
    precipChance = str(weather_result['forecasts'][0]['day']['chance_precip'])

    return "The current temperature in " + sentLocation.capitalize() + " is " + temperature + "C and the conditions are " + conditions + " with a " + precipChance + "% chance of rain."
