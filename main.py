import requests

def weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?city={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

