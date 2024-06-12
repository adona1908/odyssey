import googlemaps
import streamlit as st

# Initialize the Google Maps client with the API key
gmaps = googlemaps.Client(key=st.secrets["default"]["GOOGLE_MAPS_API_KEY"])


def fetch_route_data(departure, arrival):
    # Fetch route data using Google Maps Directions API
    directions_result = gmaps.directions(departure, arrival, mode="transit")

    if directions_result:
        # Extracting relevant details from the response
        route_info = directions_result[0]['legs'][0]
        return {
            'distance': route_info['distance']['text'],
            'duration': route_info['duration']['text'],
            'start_address': route_info['start_address'],
            'end_address': route_info['end_address'],
            'steps': [
                {
                    'instruction': step['html_instructions'],
                    'distance': step['distance']['text'],
                    'duration': step['duration']['text']
                } for step in route_info['steps']
            ]
        }
    else:
        return {'error': 'No route found'}


# Example usage (this part won't run in the module, it's for testing purpose only)
if __name__ == "__main__":
    departure = "New York, NY"
    arrival = "Los Angeles, CA"
    print(fetch_route_data(departure, arrival))
