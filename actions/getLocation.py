import urllib3
import certifi
import json

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where()
)


def getAPI(address):
    r = http.request('GET', 'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key=AIzaSyCkzpmoi6YYMNyGQqp9qqcmEwwAGbdpaUY'.format(address))

    item = r.data.decode("utf-8")
    parsed_json = json.loads(item)
    return parsed_json['results'][0]['formatted_address']

