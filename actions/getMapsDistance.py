import googlemaps
import urllib3
import certifi
import json

http =urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where()
)


def getDistance(homelocation, worklocation):
    newhomelocation = homelocation.replace(" ", "")
    newworklocation = worklocation.replace(" ", "")
    r = http.request('GET', 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={0}&destinations={1}&key=AIzaSyCkzpmoi6YYMNyGQqp9qqcmEwwAGbdpaUY'
                     .format(newhomelocation, newworklocation))
    item = r.data.decode("utf-8")
    parsed_json = json.loads(item)
    return "Today it will take you {0} to get to work and is {1} away from your home."\
        .format((parsed_json['rows'][0]['elements'][0]['duration']['text']), (parsed_json['rows'][0]['elements'][0]['distance']['text']))
    #return parsed_json



