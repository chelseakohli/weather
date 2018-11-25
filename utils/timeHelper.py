import datetime

def millisecondsToTime(time):
    convertedTime = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')
    return convertedTime