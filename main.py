import streamlit as st
import openai
import maps as gm
import googlemaps
import odyssey as od

# Initialize the OpenAI client with the API key
openai.api_key = st.secrets["default"]["OPENAI_API_KEY"]
gmaps = googlemaps.Client(key=st.secrets["default"]["GOOGLE_MAPS_API_KEY"])

# Set the page configuratio
def main():
    st.set_page_config(page_title="Odyssey", page_icon="🧭")

    st.markdown(
        """
        <style>
        .reportview-container {
            background-color: #4CAF50; /* Light grey background */
        }
        .main {
            background-color: lightblue;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .stButton button {
            background-color: #800080; /* Purple background */
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
            margin-top: 10px;
        }
        .css-1aumxhk, .css-1aumxhk, .css-18e3th9, .css-1eor8qu, .css-1ukbg1w, .css-1d391kg, .css-1v3fvcr {
            text-align: center;
            color: #333; /* Darker text color for better contrast */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.image("images/banner_image.jpg", use_column_width=True)

    #st.title("🚀 Transport Advisor 🌍", anchor=True, help="Welcome to the Transport Advisor!")
    st.markdown("<h1 style='text-align: center; color: purple;'>🚀 Transport Advisor 🌍</h1>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style="text-align: center; color: #333; font-size: 24px;">
        Welcome to your personal mobility assistant! 🚗🚌🚆🚶‍♂️<br>
        Tell us your destination, departure time, and if you're up for a walk. 🏃‍♂️💨<br>
        I'll provide you with the quickest route in no time! ⏱️✨
        </div>
        """,
        unsafe_allow_html=True
    )
    left_co, cent_co, last_co = st.columns(3)
    with cent_co:
        st.image("images/logo2.jpg")
    st.caption("Note: While we wait for your feedback to improve we won't store any data!!!.")
    #st.image("odyssey_logo.jpg", use_column_width=False, caption="Odyssey Logo", width=200)

    # Collect user inputs with unique keys
    departure = st.text_input("Departure", key="departure")
    arrival = st.text_input("Arrival", key="arrival")
    time = st.text_input("Time", key="time")
    walking = st.text_input("Walking", key="walking")

    # Handle button click event
    if st.button("Ask Odyssey!"):
        if departure and arrival and time and walking:
            response = od.transport_advisor(departure, arrival, time, walking)
            try:
                # Extract and display the response
                generated_text = response['choices'][0]['message']['content'].strip()

                # Create tabs for Directions and Map
                tab1, tab2 = st.tabs(["Directions🧭", "Map🗺"])

                with tab1:
                    st.write(generated_text)

                with tab2:
                    # Get and display route map
                    map_url = gm.get_route_map(departure, arrival)
                    if map_url.startswith("Error"):
                        st.write(map_url)
                    else:
                        st.markdown(
                            f'<iframe width="600" height="450" frameborder="0" style="border:0" src="{map_url}" allowfullscreen></iframe>',
                            unsafe_allow_html=True)

            except Exception as e:
                st.write(f"An error occurred while processing the response: {e}")
        else:
            st.write("Please provide all inputs.")


# Run the main function
if __name__ == "__main__":
    main()
