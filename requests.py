import requests
def get_garde():
    req = requests.get("http://127.0.0.1:8000/grades")
    return req