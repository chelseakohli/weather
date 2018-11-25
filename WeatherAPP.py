import tkinter
import os

#internal imports
from services.organizeWeatherData import weatherDataOrganizer
from utils.common import *
from api.openWeather import fetchWeatherData
from ui.home import *

city = input("Please enter the city to determine the weather :: ")
if __name__ == '__main__':
    try:
        data= weatherDataOrganizer(fetchWeatherData(buildURLForCity(city)))
        if data:
            printWeatherData(data)
            displayUI(data)
    except IOError:
        print('Something went wrong. Please try again.')


		
