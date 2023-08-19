import requests
import json
import os
import time


# Requests weather data from api and dumps to 'weather.json'
def get_and_dump(api_path, params):
    with open('weather.json', 'w+') as w_json:
        result = requests.get(api_path, params)
        print('GET requesting API...')
        response = result.json()
        json.dump(response, w_json, indent=4, sort_keys=True)


# Setting variables for time, api url, and parameters
# Parameters are for the API call
current_time = time.time()
API_CURRENT = 'http://api.weatherstack.com/current'
parameters = {
    'access_key': '0281837a5be96907fa57ea6e651bb7b1',
    'query': 'Big Rapids, Michigan',  # desired location for weather
    'units': 'f'  # units come back from api in Fahrenheit
}

# Checks file for data
with open('weather.json', 'r') as w_json:
    data = json.load(w_json)
    city = parameters['query'].split(',')[0]
    if city not in data['location']['name']:
        in_file = False
        print(in_file)
    else:
        in_file = True
        print('Data is in cache folder, checking most recent update...')
        m_time = os.path.getmtime('weather.json')

if not in_file or (current_time - m_time) >= 3600:
    if not in_file:
        print('Data was not in cache, updating data...')
        get_and_dump(API_CURRENT, parameters)
    if (current_time - m_time) >= 3600:
        print('Out of date data, updating data...')
        get_and_dump(API_CURRENT, parameters)


if (current_time - m_time) <= 3600 and in_file:
    print('Using data in cache...')


# Now that we have the data we want, we can pull information from our json file
with open('weather.json', 'r') as w_json:
    data = json.load(w_json)

temperature = data['current']['temperature']
time_observed = data['location']['localtime'].split(' ')[1]
uvi = data['current']['uv_index']
wind_dir = data['current']['wind_dir']
wind_speed = data['current']['wind_speed']
city = data['location']['name']
state = data['location']['region']

print('{}, {}\n{}F'.format(city, state, temperature))
