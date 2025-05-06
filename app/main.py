import os

import requests

WEATHER_API_URL = "https://api.weatherapi.com/v1"


def build_current_weather_url(query: str, key: str) -> str:
    return f"{WEATHER_API_URL}/current.json?q={query}&key={key}"


def get_weather(city: str = "Paris") -> None:
    print(f"Performing request to Weather API for city {city}...")
    url = build_current_weather_url(city, os.environ.get("API_KEY"))
    response = requests.get(url)

    current_weather = response.json()
    print(
        f"{current_weather["location"]["name"]}/"
        f"{current_weather["location"]["country"]} "
        f"{current_weather["location"]["localtime"]} "
        f"Weather: {current_weather["current"]["temp_c"]} Celsius, "
        f"{current_weather["current"]["condition"]["text"]}"
    )


if __name__ == "__main__":
    get_weather()
