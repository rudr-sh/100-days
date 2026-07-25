from datetime import datetime
import requests
import gspread
import os
from dotenv import load_dotenv
load_dotenv()
gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/1esExtxyDdTnN7Rf2QsvB6qpC3kDYukiTmJqbqfJuW7w/edit?gid=0#gid=0")
worksheet = sh.sheet1
#Getting from 100-Days API
app_id = os.getenv("APP_ID")
api_key= os.getenv("API_KEY")
health_params={
    "query":input("What did you do today?\n"),
}
headers={
    "x-app-id":app_id,
    "x-app-key":api_key
}
response=requests.post(url="https://app.100daysofpython.dev/v1/nutrition/natural/exercise",json=health_params,headers=headers)
result=response.json()
duration=result["exercises"][0]["duration_min"]
exercise=result["exercises"][0]["name"].title()
calories=result["exercises"][0]["nf_calories"]
dateandtime=datetime.now()
date=dateandtime.strftime("%d/%m/%Y")
time=dateandtime.time().strftime("%H:%M")
#Putting data in excel sheet
data=[date,time,exercise,duration,calories]
worksheet.append_row(data)
