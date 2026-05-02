import requests

def get_quiz_brain():
    params = {
        "amount": 10,
        "category": 18,
        "type": "boolean"
    }
    response = requests.get("https://opentdb.com/api.php", params=params)

    return response.json()["results"]

