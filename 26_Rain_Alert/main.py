import requests
from twilio.rest import Client
from decouple import config

# CITY = "Calgary"
CITY = "Denver"
NEXT_12_HOURS_LIMIT = 4
SNOW_WEATHER_ID = 601

# OS environment variables
# export API_KEY=asadsfdsf43r43ff3434
# api_key = os.environ.get("API_KEY")
# In python anywhere: in command type export ....; export ....; python3 main.py

APP_ID = config('OPEN_WEATHER_ID')
account_sid = config('TWILIO_ACCOUNT_SID')
auth_token = config('TWILIO_AUTH_TOKEN')
FROM_NUM = config('TWILIO_PHONE_NUM')
TO_NUM = config('MOBILE_NUM')

weather_params = {
    "q": CITY,
    "appid": APP_ID,
    "cnt": NEXT_12_HOURS_LIMIT,
}

response = requests.get("http://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()
all_weather_data = response.json().get("list")


def is_rain_snow():
    for weather_data in all_weather_data:
        for weather_type in weather_data.get("weather"):
            if weather_type.get("id") <= SNOW_WEATHER_ID:
                return True
    return False


if is_rain_snow():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain. Bring an umbrella.☔",
        from_=FROM_NUM,
        to=TO_NUM,
    )
    print(message.status)
