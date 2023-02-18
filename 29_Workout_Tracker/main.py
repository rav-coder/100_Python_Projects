import requests
from datetime import datetime
from decouple import config

GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 167
AGE = 21

APP_ID = config("APP_ID")
API_KEY = config("API_KEY")
nutritionix_header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

header_sheety = {
    "Authorization": config("HEADER"),
}

workout_in = input("Tell me the exercise you did: ")

workout_data = {
    "query": workout_in,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}
response = requests.post(url=exercise_endpoint, headers=nutritionix_header, json=workout_data)

for exercise in response.json().get("exercises"):
    excel_data = {
        "workout": {
            "date": datetime.today().strftime("%d/%m/%Y"),
            "time": datetime.today().strftime("%H:%M:%S"),
            "exercise": exercise.get("name").title(),
            "duration": exercise.get("duration_min"),
            "calories": exercise.get("nf_calories"),
        }
    }

    sheety_endpoint = "https://api.sheety.co/ca47c9deea0a4e895b4db204de01f66a/myWorkouts/workouts"

    sheety_response = requests.post(url=sheety_endpoint, json=excel_data, headers=header_sheety)
    print(sheety_response.text)
