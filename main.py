import requests
from datetime import datetime

Api_key = "bca32d32355cfd819f6e8a795d8a7a"
application_ID = "5612fd99"
API ="https://trackapi.nutritionix.com"

username = "M B"
projectname ="workouts"

sheetname = "Copy of My Workouts"
sheety_url = "https://api.sheety.co/"
Your_token = "Friday31"

INPUT = input("Type the  the exercise and for how you practice here: ")
today= datetime

API_PARAMS = {
        "query": INPUT
}

Header = {
    "x-app-id": application_ID,
    "x-app-key": Api_key
}

response = requests.post(url = "https://trackapi.nutritionix.com", json= API_PARAMS, headers= Header )
print(response.text)

# exerces = response.json()
# print(exerces)

# print(response.text)

today_date =today.strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


sheety_endpoint = f"{sheety_url}/{username}/{projectname}/{sheetname}"

Auth_header = {
    "Authorization": f" Bearer {Your_token}"
}
for exercise in exerces["Exercise"]:
    params_shetty = {
        "workout":{
            "date": today_date,
            "time": now_time,
            "exersice": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
response_sheety = requests.post(url=sheety_endpoint,json=params_shetty, headers= Auth_header)
response_sheety.raise_for_status()

print(response_sheety.text)

#
