import datetime
import requests
import urllib3
import certifi
import json
import pytz
from secrets import googleAPIKey
import calendar

response = requests.get('https://ipinfo.io').json()
loc = response["loc"]

http = urllib3.PoolManager(
    cert_reqs="CERT_REQUIRED",
    ca_certs=certifi.where()
)

r = http.request('GET', 'https://maps.googleapis.com/maps/api/timezone/json?location={0}&timestamp=1458000000&key={1}'.format(loc, googleAPIKey))

item = r.data.decode("utf-8")
parsed_json = json.loads(item)

timezone = parsed_json["timeZoneId"]
tz = pytz.timezone(timezone)
time = datetime.datetime.now(tz)

def getTime():
    return "The current time is {0}".format(str(time.time())[:5])

def getDate():
    date = time.date()
    dayDate = str(date)[8:]
    monthDate = str(date)[5:7]
    yearDate = str(date)[:4]

    months = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }

    monthName = None

    for n in months:
        if monthDate == n:
            monthName = months[n]

    return "Today is " + calendar.day_name[calendar.weekday(int(yearDate), int(monthDate), int(dayDate))] + " the " + dayDate + "th of " + monthName + ", " + yearDate
