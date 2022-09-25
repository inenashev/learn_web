import requests
import web_app.custom_secrets as custom_secrets


def weather_by_city(city_name):
    url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"

    params = {
        "key": custom_secrets.weather_token,
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
        }
    try:
        result = requests.get(url, params=params)
        result.raise_for_status()
        weather = result.json()
        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except(IndexError, TypeError):
                    return False
    except(requests.RequestException, ValueError):
        print("network error")
        return False
    return False