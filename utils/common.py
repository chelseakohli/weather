import os

def buildURLForCity(cityId):
    userAPIKey = os.environ.get('ow_api_key')#'49838e8b6cc542121457e6fc5d698463'
    unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.
    host = 'http://api.openweathermap.org/data/2.5/weather?q='

    APIURL = host + str(cityId) + '&mode=json&units=' + unit + '&APPID=' + userAPIKey
    print("API URL is --->>> {}".format(APIURL))
    return APIURL

def printWeatherData(weatherData):
    degree_symbol = '\xb0' + 'C'
    print('---------------------------------------')
    print('Weather today in: {}, {}:'.format(weatherData['city'], weatherData['country']))
    print(weatherData['temp'], degree_symbol, weatherData['sky'])
    print('Min: {}, Max: {}'.format(weatherData['temp_min'], weatherData['temp_max']))
    print('')
    print('Speed of Wind: {}, Degree: {}'.format(weatherData['wind'], weatherData['wind_deg']))
    print('Cloud: {}'.format(weatherData['cloudiness']))
    print('Humidity: {}'.format(weatherData['humidity']))
    print('Pressure: {}'.format(weatherData['pressure']))
    print('Sunrise at: {}'.format(weatherData['sunrise']))
    print('Sunset at: {}'.format(weatherData['sunset']))
    print('')
    print('ID for Weather is : {}'.format(weatherData['typeid']))
    print('Last update from the server was : {}'.format(weatherData['dt']))
    print('---------------------------------------')
    global weatherid
    weatherid = ('{}'.format(weatherData['typeid']))
    weathertype = ('{}'.format(weatherData['wtype']))
    print(weatherid)
    print(weathertype)
    weatherdata = (weatherData['wtype'])
    weathid = (weatherData['typeid'])
    wtempid = (weatherData['temp'])
    wwindid = (weatherData['wind'])
    citid = (weatherData['city'])
    countryid = (weatherData['country'])
    print("-------------------------------")