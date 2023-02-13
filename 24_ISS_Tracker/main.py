import time
import requests
from datetime import datetime
import smtplib

iss_data = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_data.raise_for_status()

iss_position = {
    "lat": float(iss_data.json().get("iss_position").get("longitude")),
    "lng": float(iss_data.json().get("iss_position").get("latitude")),
}

my_location = {
    "lat": 51.048615,
    "lng": -114.070847,
    "formatted": 0,
}


def is_iss_close():
    if abs(iss_position.get("lat") - my_location.get("lat")) <= 5 \
            and abs(iss_position.get("lng") - my_location.get("lng")) <= 5:
        return True
    return False


response_weather = requests.get("https://api.sunrise-sunset.org/json", params=my_location)
response_weather.raise_for_status()

sun = {
    "rise": int(response_weather.json().get("results").get("sunrise").split("T")[1].split(":")[0]),
    "set": int(response_weather.json().get("results").get("sunset").split("T")[1].split(":")[0]),
}


def is_night():
    current_hour = datetime.now().hour
    if current_hour >= sun.get("set") or current_hour <= sun.get("rise"):
        return True
    return False


while True:
    time.sleep(60)  # run this code every 60 seconds
    if is_iss_close() and is_night():
        print("ISS found.")
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user="email", password="pass")
            connection.sendmail(from_addr="email",
                                to_addrs="email",
                                msg=f"Subject: ISS Viewable\n\n"
                                    f"ISS Space Station is currently viewable in your location."
                                    f"It is located in {iss_position}")


