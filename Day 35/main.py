import requests
import json
api_key="8535601c219817dc78736e4ace099dd6"
data=requests.get("https://api.openweathermap.org/data/2.5/forecast?q=Delhi,India&appid=8535601c219817dc78736e4ace099dd6&cnt=4")
data.raise_for_status()
hour1=data.json()
will_rain=False
for i in range(0,4):
    id_condition=hour1["list"][i]["weather"][0]["id"]
    if id_condition<700:
        will_rain=True
if will_rain:
    print("About to rain nigga")