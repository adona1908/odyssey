import openai
import weather as we
import routes as rt

def transport_advisor(departure, arrival, time, walking):
    # Fetch weather data for Madrid
    city = 'Madrid'

    weather_data = we.fetch_weather_data(city)
    weather_info = ""

    if 'error' not in weather_data:
        weather_info = (
            f"Weather data for {city}:\n"
            f"Temperature: {weather_data['Temperature']}°C\n"
            f"Weather: {weather_data['Weather']}\n"
            f"Humidity: {weather_data['Humidity']}%\n"
            f"Pressure: {weather_data['Pressure']} hPa\n"
            f"Wind Speed: {weather_data['Wind Speed']} m/s\n"
        )
    else:
        weather_info = f"Error fetching weather data: {weather_data['error']}"

    # Fetch route data
    route_data = rt.fetch_route_data(departure, arrival)
    route_info = ""

    if 'error' not in route_data:
        route_info = (
            f"Route data:\n"
            f"Distance: {route_data['distance']}\n"
            f"Duration: {route_data['duration']}\n"
            f"Start Address: {route_data['start_address']}\n"
            f"End Address: {route_data['end_address']}\n"
            f"Steps:\n"
        )
        for step in route_data['steps']:
            route_info += f"  - {step['instruction']} ({step['distance']}, {step['duration']})\n"
    else:
        route_info = f"Error fetching route data: {route_data['error']}"

    messages = [
    {"role": "system",
     "content": (
         "Situation: You are a traveling and weather assistant. Your task is to provide recommendations on the fastest "
         "and best way to reach the destination from the departure point, considering the weather conditions and the user's "
         "capability to walk. You will be given two datasets: one containing weather data and the other containing possible "
         "routes, including modes of transportation, departure times, and destinations. The user will give you the departure "
         "and arrival points, the time of departure, and whether they are willing to walk. You will then provide the best "
         "route for the user, considering the weather conditions and the user's capability to walk. Analyze the weather forecasts "
         "and the maps for the city of Madrid from the link that the assistance message will provide to give recommendations. "
         "Always add in the output the total time of the trip."
     )},
    {"role": "user",
     "content": weather_info},
    {"role": "user",
     "content": route_info},
    {"role": "user",
     "content": (
         f"I would like to travel from {departure} to {arrival} at {time} and I am willing to walk: {walking}."
     )}
]


    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response