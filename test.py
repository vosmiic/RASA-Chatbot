import pyowm

owm = pyowm.OWM('9fe0a2cf68f89670ce2edf268dbfa827')


observation = owm.weather_at_place("brighton")
print(observation.get_weather())


