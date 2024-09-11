import requests

def get(url: str):
    response = requests.get(url)
    return response.json()