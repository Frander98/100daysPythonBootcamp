# Exercise register with NLP
import requests
import os
from datetime import datetime

# vars related to date and time
today = datetime.now()
now = datetime.now()

# authentication, endpoints and parameters
API_KEY = os.environ["API_KEY"]
APP_ID = os.environ["APP_ID"]
BEARER_AUTH = os.environ["BEARER_AUTH"]

# exercise_endpoint is for posting exercises with NLP
exercise_endpoint_post = "https://trackapi.nutritionix.com/v2/natural/exercise"

# sheet_endpoint is for adding new rows to the table
exercise = input("What exercise did you do?: ")
sheet_endpoint = "https://api.sheety.co/d936b75b660e24ab820cc18a126c597b/historicoEjercicios/workouts"
nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}
auth_header = {
    "Authorization": f"Bearer {BEARER_AUTH}",
}
nutritionix_post_body = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 84,
    "height_cm": 171,
    "age": 23
}


def run():
    response = requests.post(url=exercise_endpoint_post, json=nutritionix_post_body,
                             headers=nutritionix_headers)
    data = response.json()
    exercise_data = data["exercises"]
    # sheet_inputs = {
    # "workout": {
    #     "date": today.strftime("%d/%m/%Y"),
    #     "time": now.strftime("%X"),
    #     "exercise": exercise_data["name"].title(),
    #     "duration": exercise_data["duration_min"],
    #     "calories": exercise_data["nf_calories"]
    #     }
    # }
    # add a row to the table
    for exercise_info in exercise_data:
        sheet_inputs = {
            "workout": {
                "date": today.strftime("%d/%m/%Y"),
                "time": now.strftime("%X"),
                "exercise": exercise_info["name"].title(),
                "duration": exercise_info["duration_min"],
                "calories": exercise_info["nf_calories"]
            }
         }

    response = requests.post(url=sheet_endpoint, json=sheet_inputs,
                             headers=auth_header)
    response.raise_for_status()
    data = response.json()

    print(data)


# Entry point of the script
if __name__ == '__main__':
    run()
