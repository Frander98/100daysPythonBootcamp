import requests
import os
from twilio.rest import Client


# Account data from twilo
account_sid = os.environ["TWILIO_ID"]
auth_token = os.environ["TWILIO_TOKEN"]
api_key = os.environ["TWILIO_KEY"]

# Data from Open Weather Map, One call API
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"


# Parameters requested from open weather map in order to get the data,
# check the documentation in https://openweathermap.org/api/one-call-api
# La Palma coor: 10.50288632587581, -84.69365560845287
# La Fortuna coor 10.471230, -84.641830,

request_param = {
    "lat": 10.50288632587581,
    "lon": -84.69365560845287,
    "exclude": "current,minutely,daily,alerts",
    "appid": api_key,
    "lang": "sp"
}


# run function, passed into the entry point in order to execute the program
def run():
    response = requests.get(url=OWM_ENDPOINT, params=request_param)
    response.raise_for_status()
    weather_data = response.json()
    weather_slice = weather_data["hourly"][:20]
    codes = []
    detail_hour_descriptions = []
    hour_and_description = {}

    # To add the codes of the weather to [codes]
    for hour_data in weather_slice:
        codes.append(hour_data["weather"][0]["id"])
        detail_hour_descriptions.append(hour_data["weather"][0]["description"])

    will_rain_or_not = False
    for code in codes:
        if code < 700:
            will_rain_or_not = True

    if will_rain_or_not:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"Hola, por favor lleva paraguas porque va a llover.\n"
                 "☔\n"
                 "Detalle por hora: "
                 f"{detail_hour_descriptions}"
                 "",
            from_='+14092077394',
            to='+50689083124',
        )
    print(message.status)


# Entry point
if __name__ == '__main__':
    run()

# ----------* END OF THE SCRIPT *----------
