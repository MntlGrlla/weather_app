import requests
import json
from json.decoder import JSONDecodeError
import os
import time


# Requests weather data from weatherstack api and dumps to 'weather.json'
def get_and_dump(api_path, params):
    with open('weather.json', 'w+') as w_json:
        result = requests.get(api_path, params)
        print('GET requesting API...')
        response = result.json()
        json.dump(response, w_json, indent=4, sort_keys=True)


# returns in_file = True if correct data is present, returns in_file = False if correct data is not present
def data_check():
    with open('weather.json', 'r') as w_json:
        try:
            data = json.load(w_json)
            city = parameters['query'].split(',')[0]
            if city not in data['location']['name']:
                in_file = False
                print(in_file)
            else:
                in_file = True
                print('Data is in cache folder, checking most recent update...')
        except JSONDecodeError:
            in_file = False
            pass
    return in_file


# Conditional block to update data if it is not present, or if it has been an hour since data was last updated
def recent_or_missing(in_file, current_time, mod_time, parameters):
    if not in_file or (current_time - mod_time) >= 3600:
        if not in_file:
            print('Data was not in cache, updating data...')
            get_and_dump(API_CURRENT, parameters)
        if current_time - mod_time >= 3600:
            print('Out of date data, updating data...')
            get_and_dump(API_CURRENT, parameters)
    with open('weather.json', 'r') as w_json:
        data = json.load(w_json)

    return data


# Updates weather information, calls recent_or_missing() to check accuracy of data
def update_weather_data(query, in_file, current_time, mod_time, parameters):
    parameters['query'] = query
    data = recent_or_missing(in_file, current_time, mod_time, parameters)
    return data


# Stores parameters dictionary in 'parameters.json'
def store_parameters(query, parameters):
    parameters['query'] = query
    with open('parameters.json', 'w+') as param_json:
        json.dump(parameters, param_json, indent=4, sort_keys=True)


# Opens parameters.json file and returns the data
def open_parameters():
    with open('parameters.json', 'r') as param_json:
        parameters = json.load(param_json)
    return parameters


# Setting variables for time, api url, and parameters
# Parameters are for the API call
current_time = time.time()
API_CURRENT = 'http://api.weatherstack.com/current'
parameters = open_parameters()

# initializing mod_time with the timestamp from last modification of the file 'weather.json'
mod_time = os.path.getmtime('weather.json')
in_file = data_check()

data = recent_or_missing(in_file, current_time, mod_time, parameters)

if (current_time - mod_time) <= 3600 and in_file:
    print('Using data in cache...')

temperature = data['current']['temperature']
time_observed = data['location']['localtime'].split(' ')[1]
uvi = data['current']['uv_index']
wind_dir = data['current']['wind_dir']
wind_speed = data['current']['wind_speed']
city = data['location']['name']
state = data['location']['region']

print('{}, {}\n{}F'.format(city, state, temperature))
