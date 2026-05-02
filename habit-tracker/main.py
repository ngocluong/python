from wsgiref import headers

import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "ngocluong"
TOKEN = "HjAis22dmx12"
GRAPH_ID = "graph1"
# params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# response = requests.post(url=pixela_endpoint, json=params)
# print(response.json())
headers = {
    "Content-Type": "application/json",
    "X-USER-TOKEN": TOKEN
}

params = {
    "id": GRAPH_ID,
    "name": "learn python",
    "unit": "section",
    "color": "shibafu",
    "type": "int"
}

# res = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs", headers=headers, json=params)
# print(res.json())
now = datetime.now()
g_params = {
    "date": str(now.strftime("%Y%m%d")),
    "quantity": input("how many section you study today?"),

}
g_res = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}", headers=headers, json=g_params)
print(g_res.json())