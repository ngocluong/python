import os

import requests
from datetime import datetime

BASE_URL = "https://app.100daysofpython.dev"
now = datetime.now()

HEADER={
    "x-app-id": "app_67611edc68b240c6a56f6587",
    "x-app-key": "nix_live_FEOCGauYQoTXIX88Mpa73Yvn7JGfti2N"
}

query = input("Tell me which exercise you did?")
response = requests.post(f"{BASE_URL}/v1/nutrition/natural/exercise",
                         headers=HEADER, json={"query":query})

SHEETY_URL = "https://api.sheety.co/da9f0cfcac6fbbbcb78e0a0f2df67d14/myWorkouts/workouts"
SHEETY_TOKEN = "thiIstokem12"
SHEETY_HEADER = {
    "Authorization": "Bearer " + SHEETY_TOKEN,
}
data = response.json()["exercises"][0]
data_for_sheet = {
    "workout": {
        "date": str(now.strftime("%d/%m/%Y")),
        "time": now.strftime("%H:%M:%S"),
        "exercise": data["name"],
        "duration": data["duration_min"],
        "calories": data["nf_calories"],
    }
}
s_response = requests.post(SHEETY_URL,headers=SHEETY_HEADER, json=data_for_sheet)