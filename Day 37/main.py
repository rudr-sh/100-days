import requests
from datetime import datetime
username="rusifer"
token="Hello@12345678"
pixela_endpoint = "https://pixe.la/v1/users"
user_params={
    "token":"Hello@12345678",
    "username":"rusifer",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{username}/graphs"
graph_params={
    "id":"graph1",
    "name":"Weight graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}
headers={
    "X-USER-TOKEN": token
}
# response=requests.post(url=graph_endpoint,json=graph_params, headers=headers)
# print(response.text)

today = datetime.now()
graph_update_endpoint=f"{graph_endpoint}/graph1"
graph_update_params={
    "date": today.strftime("%Y%m%d"),
    "quantity":"100",
}
# response=requests.post(url=graph_update_endpoint,json=graph_update_params,headers=headers)
# print(response.text)
#update a pixel 
update_pixel_endpoint=f"{graph_update_endpoint}/20260722"
update_pixel_params={
    "quantity":"100"
}
response=requests.put(url=update_pixel_endpoint,json=update_pixel_params,headers=headers)
print(response.text)