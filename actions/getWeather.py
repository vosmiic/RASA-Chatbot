import pywapi

def getLocationWeather(sentLocation):
    global precipChance
    location = pywapi.get_location_ids(sentLocation)
    weather_result = pywapi.get_weather_from_weather_com(next(iter(location)))
    conditions = str(weather_result['current_conditions']['text'])
    temperature = str(weather_result['current_conditions']['temperature'])
    precipChance = str(weather_result['forecasts'][0]['day']['chance_precip'])

    return "The current temperature in " + sentLocation.capitalize() + " is " + temperature + "C and the conditions are " + conditions + " with a " + precipChance + "% chance of rain."


def getRainChance(sentLocation):
    getLocationWeather(sentLocation)
    if int(precipChance) < 50:
        return "There is a {0}% chance of rain today, so I don't think it will rain today.".format(precipChance)
    else:
        return "There is a {0}% chance of rain today, so I think it will rain today.".format(precipChance)


def getTomorrowWeather(sentLocation):
    location = pywapi.get_location_ids(sentLocation)
    weather_result = pywapi.get_weather_from_weather_com(next(iter(location)))

    averageTemp = ((int(weather_result['forecasts'][1]['high'])) + (int(weather_result['forecasts'][1]['low']))) / 2
    rainChance = int(weather_result['forecasts'][1]['day']['chance_precip'])
    conditions = str(weather_result['forecasts'][1]['day']['text'])

    return "{0} with an average temperature of {1}C and with a {2}% chance of rain.".format(conditions, averageTemp, rainChance)
