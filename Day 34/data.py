import requests 
import html
paramerters={   
             "amount": 10,
             "type": "boolean"}
response = requests.get("https://opentdb.com/api.php",params=paramerters)
response.raise_for_status()
question_data=response.json()["results"]