import requests
import streamlit as st

# Function to fetch weather data
def fetch_weather_data(city_name):
    api_key = st.secrets["default"]["WEATHER_API_KEY"]
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # To get temperature in Celsius
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            'Temperature': data['main']['temp'],
            'Weather': data['weather'][0]['description'],
            'Humidity': data['main']['humidity'],
            'Pressure': data['main']['pressure'],
            'Wind Speed': data['wind']['speed']
        }
    else:
        return {'error': 'Could not fetch data'}

# Example usage
city = 'London'
weather_data = fetch_weather_data(city)

if 'error' not in weather_data:
    print(f"Weather data for {city}:")
    print(f"Temperature: {weather_data['Temperature']}°C")
    print(f"Weather: {weather_data['Weather']}")
    print(f"Humidity: {weather_data['Humidity']}%")
    print(f"Pressure: {weather_data['Pressure']} hPa")
    print(f"Wind Speed: {weather_data['Wind Speed']} m/s")
else:
    print(weather_data['error'])

# Example replacement of the user content
user_content = {
    "role": "user",
    "content": (
        "Here are the links to the datasets: "
        "[Weather Data](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data) "
        "and [Routes Data](https://www.kaggle.com/nowke9/transport-features-data)."
    )
}

# Function to include OpenWeatherMap data in the user content
def update_user_content_with_weather(user_content, city):
    weather_data = fetch_weather_data(city)
    if 'error' not in weather_data:
        weather_info = (
            f"Weather data for {city}:\n"
            f"Temperature: {weather_data['Temperature']}°C\n"
            f"Weather: {weather_data['Weather']}\n"
            f"Humidity: {weather_data['Humidity']}%\n"
            f"Pressure: {weather_data['Pressure']} hPa\n"
            f"Wind Speed: {weather_data['Wind Speed']} m/s\n"
        )
        user_content['content'] = f"{user_content['content']}\n\n{weather_info}"
    else:
        user_content['content'] = f"{user_content['content']}\n\nError: {weather_data['error']}"
    return user_content

# Update user content with weather data
city = 'Madrid'
updated_content = update_user_content_with_weather(user_content, city)
print(updated_content['content'])
