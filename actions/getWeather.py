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

def getForecast(date, sentLocation):
    location = pywapi.get_location_ids(sentLocation)
    weather_result = pywapi.get_weather_from_weather_com(next(iter(location)))

    month = str(date[5:7])
    day = str(date[8:10])
    if str(day).startswith("0"):
        day = date[9:10]

    months = {
        "01": "Jan",
        "02": "Feb",
        "03": "Mar",
        "04": "Apr",
        "05": "May",
        "06": "Jun",
        "07": "Jul",
        "08": "Aug",
        "09": "Sep",
        "10": "Oct",
        "11": "Nov",
        "12": "Dec"
    }

    monthName = None

    for n in months:
        if month == n:
            monthName = months[n]

    for x in weather_result['forecasts']:
        if str(x['date']) == monthName + " " + day:
            conditions = x['day']['text']
            precipChance = x['day']['chance_precip']
            averageTemp = (int(x['high']) + int(x['low'])) / 2

            return "On {0} {1} it will be {2} with a {3}% chance of rain, with an average temperature of {4}.".format(day, monthName, conditions, precipChance, averageTemp)

    return "I cannot tell the forecast for that day."
