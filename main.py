import requests
from datetime import datetime


pixela_endpoint = "https://pixe.la//v1/users"
USERNAME ="tugrul1"
TOKEN = "gegejujutsu123"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
#response = requests.post(url=pixela_endpoint,json=user_params)
#print(response.text)
#pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
#response = requests.post(url=pixela_graph_endpoint,json=graph_config, headers=headers)

today = datetime.now().date()

test = today.strftime("%Y%m%d")
print(test)


#graph_pixel_post =f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
pix_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today?"),
}

#response_pix = requests.post(url=graph_pixel_post,json=pix_config, headers=headers)
#print(response_pix.text)
new_pixel_data = {
    "quantity": "20"
}
#response_put = requests.put(url=f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{test}", json= new_pixel_data, headers=headers)
#print(response_put.text)

response = requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{test}", headers=headers)
print(response.text)