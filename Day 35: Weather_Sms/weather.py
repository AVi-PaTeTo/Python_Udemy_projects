import requests
from twilio.rest import Client

#things necessary (all should be string):
SID   = "None" #available on twilio
TOKEN = "None"
T_NUM = "None" #twilio number
R_NUM = "None" #reciever's number


#Twilio details
account_sid = SID
auth_token = TOKEN
client = Client(account_sid, auth_token)

#api structure: api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}

#parameters for api request
parameters= {
    "lat": 51.507351, # use your lat and long
    "lon": -0.127758,
    "appid": "5b5d3cf45cbf6da83b1e3fb23c587090",
    'cnt': 4
}

will_rain = False

#get data from weather api,
response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=parameters)
response.raise_for_status()
data = response.json()
for x in data["list"]:
    if x["weather"][0]["id"] <= 700:
        will_rain =True

if will_rain:
    message = client.messages.create(
    from_= T_NUM,
    body="Looks like it's gonna rain today, dont forget your umbrella",
    to= R_NUM
    )
