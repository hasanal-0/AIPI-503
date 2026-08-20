# Week 5 - Day 2: Streamlit

A simple streamlit page that fetches and displays current weather data for any city using the OpenWeatherMap API.


## What It Does

- Prompts the user to enter the name of a city
- Calls the OpenWeatherMap API to retrieve current weather data for that city
- Displays the following, with color-coded output for readability:
  - Temperature (°C)
  - Humidity
  - Weather description
  - Wind speed and direction
  - Latitude and longitude

## Install
- Install the following if you do not have:
    - import requests
    - import os
    - from dotenv import load_dotenv
    - import streamlit as st

## Usage

Run the script:
```bash
python main.py
```

You'll be prompted to enter a city name:
```
Welcome to the Weather App!
Below you will enter in a city of your choice to see what the current weather is like
Enter in the city: Dubai
```

Example output:
```
In Dubai, AE it is 36.96°C with a humidity of 47, and clear sky. 
The current wind is: 2.57 m/s, in the direction of 80° 
The exact location is: lat 25.2582, lon 55.3047
```
  
## Project Structure

```
week5-day2/
├── main.py         # Main application script
├── .env            # API key (not committed)
├── .gitignore      # Ignores .env and .vscode/ (not committed)
└── README.md       # This file
```
