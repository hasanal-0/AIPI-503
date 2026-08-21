# Week 5 - Day 4: GitHub Team Etiquette

A simple streamlit page that fetches and displays current weather data for any city using the OpenWeatherMap API.


## What It Does

- Prompts the user to enter the name of a city
- Calls the OpenWeatherMap API to retrieve current weather data for that city
- Displays the following:
  - City name and country
  - Temperature (°C)
  - Humidity
  - Weather description
  - Wind speed and direction
  - Latitude and longitude
  - Shows a world map image after the weather results are displayed

## Python Version

This project was built and tested with **Python 3.11**.

## Install
- Install the following if you do not have:
    - requests
      - pip install requests
    - streamlit
      - pip install streamlit
    - dotenv
      - pip install python-dotenv

## How to run locally
1. Install all required dependices listed above 
2. Set up a .env with your API key from 'https://openweathermap.org/api'
3. run this command in your terminal ```streamlit run "c:<path to your folder>/main.py"```
4. Output should look similar to the following on the streamlit page: 

You'll be prompted to enter a city name:
```
Welcome to the Weather App!
Below you will enter in a city of your choice to see what the current weather is like
Enter in the city: <Ex: Dubai>
```

Example output:
```
In Dubai, AE it is 36.96°C with a humidity of 47, and clear sky. 
The current wind is: 2.57 m/s, in the direction of 80° 
The exact location is: lat 25.2582, lon 55.3047
```

## How to run the web app
- The web app will use a streamlit secrect for its API, so simply go to the following website: 
``` ```
- the page will look the same as when it was run locally

## Usage

Run the script:
```bash
python main.py
```


  
## Project Structure

```
week5-day4/
├── main.py               # Main application script
├── .env                  # API key (not committed)
├── .gitignore            # Ignores .env and .vscode/ (not committed)
├── requirements.txt      # lists the required packages and their versions
└── README.md             # This file
```
