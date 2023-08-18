# weather_app
building a weather app using weatherstack API

Currently working on building a weather application using python. I would also like to have a proper GUI with this application. Eventually it will all be there. 

The 'weather.json' file is essentially a cache so that I don't have to keep using up API requests to test my build.
  The 'weather.py' file is my main file with the api requests. It checks if the 'weather.json' file has information from the current city in the query.
If the requested city is in the json file, it will not send an API request to weatherstack. Instead it will use the existing data in the json file. Eventually, I would
like to have it also check the time from the previous get request. If less than an hour has passed, I would like to use the information that is in the file. If more 
than an hour has passed, I will have the program send a new api request, dump that data into the json file, and use it for the application. 
