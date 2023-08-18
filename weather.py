import requests
import json

API_CURRENT = 'http://api.weatherstack.com/current'
parameters = {
    'access_key': '0281837a5be96907fa57ea6e651bb7b1',
    'query': 'Iron Mountain, Michigan',
    'units': 'f'
}

with open('weather.json', 'r') as w_json:
    data = json.load(w_json)
    city = parameters['query'].split(',')[0]
    if city not in data['location']['name']:
        in_file = False
    else:
        in_file = True

if not in_file:
    with open('weather.json', 'w+') as w_json:
        w_result = requests.get(API_CURRENT, parameters)
        w_response = w_result.json()
        json.dump(w_response, w_json, indent=4, sort_keys=True)

print(in_file)
