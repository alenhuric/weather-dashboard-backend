import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def fetch_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    r = requests.get(url)
    data = r.json()
    if r.status_code != 200 or "main" not in data:
        raise Exception(data.get("message", "Error fetching weather"))
    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"]
    }
