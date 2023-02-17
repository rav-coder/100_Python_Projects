import requests
from decouple import config
from datetime import datetime

USERNAME = config('USER')
TOKEN = config("TOKEN")
pixela_endpoint = "https://pixe.la/v1/users"
# URL = "https://pixe.la/@r8hj"

header = {
    "X-USER-TOKEN": TOKEN,
}

user_params = {
    "token": "token",
    "username": "name",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_config = {
    "id": "test-graph",
    "name": "Meditation Graph",
    "unit": "Hours",
    "type": "float",
    "color": "shibafu",
}
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)


meditation_graph_endpoint = graph_endpoint + f"/{graph_config.get('id')}"
today = datetime.today()
# print(today.strftime("%Y%m%d"))
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1.5",
    "optionalData": "{\"Quote\":\"Who am I?\"}"
}
response = requests.post(url=meditation_graph_endpoint, json=pixel_data, headers=header)
print(response.text)


date_endpoint = meditation_graph_endpoint + f"/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "1",
    "optionalData": "{\"Quote\":\"Who am I?\"}"
}
# response = requests.put(url=date_endpoint, json=new_pixel_data, headers=header)
# print(response.text)

# response = requests.delete(url=date_endpoint, headers=header)
# print(response.text)
