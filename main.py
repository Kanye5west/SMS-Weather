import requests
from twilio.rest import Client


account_sid = 'acc_sid'
auth_token = 'auth token'

Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "api_key"

parameters = {
    "lat": 14,
    "lon": 121,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(Endpoint, params= parameters)
weather_data = response.json()


will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(body= "Bring an Umbrella!, This is from Weather SMS :)",
                                     from_= 'from number',
                                     to= 'end number')

    print(message.sid)
