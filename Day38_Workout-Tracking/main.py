import requests
from datetime import datetime
from config import API_ID, API_KEY, USER, PASS, GENDER, WEIGHT_KG, HEIGHT, AGE

basic = (USER, PASS)

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheet_endpoint= "https://api.sheety.co/f7fbe5ee97535c2c9d4750651961ea5f/workoutTracking/workouts"

headers= {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

exercise_text = input("Tell me which exercises you did: ")

user_params= {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=user_params, headers=headers)
response.raise_for_status()
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth= basic)
    print(sheet_response.text)