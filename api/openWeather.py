import requests
import json
import sys

def fetchWeatherData(apiURL):
    # timeout is added for 3 seconds. If in 3 seconds request is not completed the program will terminate
    response = requests.get(apiURL, timeout=3)
    if response.status_code == 200:
        print("Request to openweather was successful. HTTP Status Code: " + str(response.status_code))
    elif response.status_code != 200:
        print("Request to openweather was unsuccessful. HTTP Status Code: "+ str(response.status_code))
        response.raise_for_status()
    return json.loads(response.content)