from requests import HTTPError

from services.organizeWeatherData import weatherDataOrganizer
from utils.common import *
from api.openWeather import fetchWeatherData
from ui.home import *

city = input("Please enter the city to determine the weather :: ")
if __name__ == '__main__':
    try:
        weatherData = weatherDataOrganizer(fetchWeatherData(buildURLForCity(city)))
        if weatherData is not None:
            displayUI(weatherData)
    except (IOError,HTTPError) as error:
        if error.response.status_code == 404:
            print('Invalid City/Country. Please try again.')
            exit()
        print('Something went wrong. Please try again. Error: {}'.format(error))
