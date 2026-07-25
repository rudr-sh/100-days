import requests
from datetime import datetime,timezone
import smtplib
import time
parameters={
    "lat":12.971599,
    "lng":77.594566,
    "formatted":0,
}
response1 =requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response1.raise_for_status()
data1=response1.json()
sunrise=int(data1["results"]["sunrise"].split("T")[1].split(":")[0])
sunset=int(data1["results"]["sunset"].split("T")[1].split(":")[0])

response2=requests.get("http://api.open-notify.org/iss-now.json")
response2.raise_for_status()
data2=response2.json()
iss_position=(data2["iss_position"]["longitude"],data2["iss_position"]["latitude"])
print(iss_position)
time_now=datetime.now(timezone.utc).hour

if not sunrise <= time_now <= sunset:
    if abs(float(iss_position[0]) - parameters["lng"]) <= 5 and abs(float(iss_position[1]) - parameters["lat"]) <= 5:
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user="pythonrudrsh01@gmail.com",password="mnsm bgsa gfct ckmq")
            connection.sendmail(from_addr="pythonrudrsh01@gmail.com",to_addrs="rusifer2002@gmail.com",msg="Subject: Look Up!!\n\nThe ISS is above your head and you can see it right now.")
else:
    print("It's day time cannot see ISS")