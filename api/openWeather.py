import requests
import json

# def data_fetch(full_api_url):
#     url = urllib.request.urlopen(full_api_url)
#     output = url.read().decode('utf-8')
#     raw_api_dict = json.loads(output)
#     url.close()
#     return raw_api_dict

def fetchWeatherData(apiURL):
    req = requests.get(apiURL)
    if req.status_code == 200:
        print("Request to openweather was successful. HTTP Status Code: " + str(req.status_code))
    elif (req.status_code != 200):
        print("Request to openweather was unsuccessful. HTTP Status Code: "+ str(req.status_code))
    return json.loads(req.content)
