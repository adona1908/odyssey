import googlemaps
import streamlit as st

# Initialize the Google Maps client with the API key
gmaps = googlemaps.Client(key=st.secrets["default"]["GOOGLE_MAPS_API_KEY"])

def get_route_map(departure, arrival):
    directions_result = gmaps.directions(departure, arrival)

    if directions_result:
        route = directions_result[0]
        map_url = generate_map_url(route)
        return map_url
    else:
        return "Error: No routes found"

def generate_map_url(route):
    origin = route['legs'][0]['start_location']
    destination = route['legs'][0]['end_location']
    base_url = "https://www.google.com/maps/embed/v1/directions"
    params = {
        "origin": f"{origin['lat']},{origin['lng']}",
        "destination": f"{destination['lat']},{destination['lng']}",
        "key": st.secrets["default"]["GOOGLE_MAPS_API_KEY"]
    }

    map_url = f"{base_url}?origin={params['origin']}&destination={params['destination']}&key={params['key']}"
    return map_url
