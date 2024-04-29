from dotenv import load_dotenv
import os
import requests
from requests.auth import HTTPBasicAuth
import datetime as dt


GENDER = "male"
WEIGHT = 68
HEIGHT = 170
AGE = 24

load_dotenv("./workout_tracking/.env")

APP_ID = os.getenv('NUTRI_ID')
API_KEY = os.getenv('NUTRI_KEY')
USER = os.getenv('SHEETY_USER')
PASS = os.getenv('SHEETY_PASS')
TOKEN = os.getenv('SHEETY_TOKEN')

nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = f"https://api.sheety.co/{TOKEN}"

nutri_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

nutri_parameters = {
    "query": "",
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}
#blank dictionary to hold exercise stats
sheety_entry = {
        "workout":{
            "date": "",
            "time": "",
            "exercise": "",
            "duration": "",
            "calories": ""
        }
    }

query = input("Tell us what exercise you did: ")
nutri_parameters["query"] = query
nutri_response = requests.post(nutri_endpoint, json=nutri_parameters, headers=nutri_headers)
nutri_data = nutri_response.json()

#list of exercises done
activities = nutri_data["exercises"]


for exercise in activities:
    #fill up the dictionary before uploading to sheety
    sheety_entry["workout"]["date"] = dt.date.today().strftime("%d/%m/%Y")
    sheety_entry["workout"]["time"] = dt.datetime.now().strftime("%H:%M:%S")
    sheety_entry["workout"]["exercise"] = exercise["name"].title()
    sheety_entry["workout"]["duration"] = exercise["duration_min"]
    sheety_entry["workout"]["calories"] = exercise["nf_calories"]

    sheety_response = requests.post(sheety_endpoint, json=sheety_entry, auth=(USER,PASS))
