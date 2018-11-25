from utils.timeHelper import millisecondsToTime

def weatherDataOrganizer(rawJSONPayload):
    data = dict(
        city=rawJSONPayload.get('name'),
        country=rawJSONPayload.get('sys').get('country'),
        temp=rawJSONPayload.get('main').get('temp'),
        temp_max=rawJSONPayload.get('main').get('temp_max'),
        temp_min=rawJSONPayload.get('main').get('temp_min'),
        humidity=rawJSONPayload.get('main').get('humidity'),
        pressure=rawJSONPayload.get('main').get('pressure'),
        sky=rawJSONPayload['weather'][0]['main'],
        sunrise=millisecondsToTime(rawJSONPayload.get('sys').get('sunrise')),
        sunset=millisecondsToTime(rawJSONPayload.get('sys').get('sunset')),
        wind=rawJSONPayload.get('wind').get('speed'),
        wind_deg=rawJSONPayload.get('wind').get('deg'),
        dt=millisecondsToTime(rawJSONPayload.get('dt')),
        cloudiness=rawJSONPayload.get('clouds').get('all'),
        typeid=rawJSONPayload['weather'][0]['id'],
        wtype=rawJSONPayload['weather'][0]['description']
    )
    return data