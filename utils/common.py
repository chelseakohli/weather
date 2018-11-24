import os

def buildURLForCity(cityId):
    userAPIKey = os.environ.get('ow_api_key')#'49838e8b6cc542121457e6fc5d698463'
    unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.
    host = 'http://api.openweathermap.org/data/2.5/weather?q='

    APIURL = host + str(cityId) + '&mode=json&units=' + unit + '&APPID=' + userAPIKey
    print("API URL is --->>> {}".format_map(APIURL))
    return APIURL
