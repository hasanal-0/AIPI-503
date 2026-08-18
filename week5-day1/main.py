"""
Week 5 - Day 1: API Calls
=================================================
Today I will call the weather API:
  * It will ask the user for the city they are in
  * Then display data based off what the user has entered
"""

import requests
import os
from dotenv import load_dotenv
import json
from colorama import Fore, Style, init

init(autoreset=True)
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

def weather_call(city):
    """
    Using the city name given by the user we will return the weather in that city
    """
    """
    Retrieves the current weather data for a given city.

    Parameters:
        city (str): Name of the city to get weather data for.

    Returns:
        Temp in Celsius, Humidity, and Description
    """
    url = "https://api.openweathermap.org/data/2.5/weather?"
    
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    #print(json.dumps(data, indent=2))    
    
    city_name = data["name"]
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    wind_deg = data["wind"]["deg"]
    lat = data["coord"]["lat"]
    lon = data["coord"]["lon"]
    country = data["sys"]["country"]
        
    print(
        Fore.CYAN + f"\nIn {city_name}, {country} " +
        Style.RESET_ALL + "it is " +
        Fore.YELLOW + f"{temp}°C " +
        Style.RESET_ALL + "with a humidity of " +
        Fore.BLUE + f"{humidity}, " +
        Style.RESET_ALL + "and " +
        Fore.MAGENTA + f"{description}. "
    )

    print(Fore.GREEN + f"The current wind is: {wind_speed} m/s, in the direction of {wind_deg}° ")
    print(Fore.LIGHTBLUE_EX + f"The exact location is: lat {lat}, lon {lon}")



print(Fore.GREEN + "Welcome to the Weather App!")
print(Fore.LIGHTMAGENTA_EX +  "Below you will enter in a city of your choice to see what the current weather is like")
user_input = input("Enter in the city: ")
weather_call(user_input)
