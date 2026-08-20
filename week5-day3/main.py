"""
Week 5 - Day 3: HuggingFace
=================================================
Today I will call the weather API and using Streamlit:
  * It will ask the user for the city they are in streamlit
  * Then display data based off what the user has entered in streamlit
  * All of this will be on https://streamlit.io/cloud  since huggignface does not work
"""

import requests
import streamlit as st

API_KEY = st.secrets["WEATHER_API_KEY"]

def weather_call(city):
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
        
    city_name = data["name"]
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    wind_deg = data["wind"]["deg"]
    lat = data["coord"]["lat"]
    lon = data["coord"]["lon"]
    country = data["sys"]["country"]
        
    st.subheader(f"{city_name}, {country}")
    st.write(f"It is {temp}°C with a humidity of {humidity}, and {description}.")
    st.write(f"The current wind is: {wind_speed} m/s, in the direction of {wind_deg}°")
    st.write(f"The exact location is: lat {lat}, lon {lon}")



st.title("Welcome to the Weather App!")
st.subheader("Below you will enter in a city of your choice to see what the current weather is like")
city = st.text_input("Enter in the city:")

if st.button("See Weather"):
    weather_call(city)
    st.image(
        "https://media.sciencephoto.com/c0/05/35/22/c0053522-800px-wm.jpg",
        caption="World Map",
        use_container_width=True
    )
