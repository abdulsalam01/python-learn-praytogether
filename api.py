import requests
import os
from dotenv import load_dotenv, dotenv_values

# Loading variables from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = f"https://api.weatherapi.com/v1/"

def requestWeather(location, enable_air_condition):
    # Define URL based on location and air condition.
    url = normalizeUrl(False, location, {"aqi": enable_air_condition})
    # Do a request.
    response = requests.get(url)
    # Parsing to JSON.
    return response.json()

def requestForecast(location, days, alerts):
    # Define URL based on location and air condition.
    url = normalizeUrl(True, location, {"days": days, "alerts": alerts, "aqi": "yes"})
    # Do a request.
    response = requests.get(url)
    # Parsing to JSON.
    return response.json()

def normalizeUrl(is_forecast, location, attributes = {}):
    partialUrl = f"current.json?key={API_KEY}"
    partialUrl = partialUrl + "&aqi=" + attributes["aqi"]

    if is_forecast:
        partialUrl = f"forecast.json?key={API_KEY}"
        partialUrl = partialUrl + "&days=" + attributes["days"] + "&alerts=" + attributes["alerts"]

    # Define URL based on location and air condition.
    url = BASE_URL + partialUrl + "&q=" + location
    return url

# response = requestWeather("Bandung", "yes")
responseForecast = requestForecast("Bandung", "1", "yes")

for inHours in responseForecast['forecast']['forecastday'][0]['hour']:
    print("tanggal " + inHours["time"] + " kelembaban: " + str(inHours["humidity"]))