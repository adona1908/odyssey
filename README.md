﻿# Transport Advisor 🚀🌍

Welcome to the Transport Advisor! This Streamlit application helps you find the best route for your travels in Madrid, considering the weather conditions and your preferences for walking.

## Features

- Provides the fastest and best route from departure to destination.
- Considers current weather conditions in Madrid.
- Displays detailed travel steps and total travel time.
- Interactive map visualization for the route.

## Installation

1. Clone this repository:
    ```sh
    git clone (https://github.com/adona1908/odyssey)
    cd your-repository
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Add your API keys to the `secrets.toml` file located in the `.streamlit` directory:
    ```toml
    [default]
    OPENAI_API_KEY = "your_openai_api_key"
    GOOGLE_MAPS_API_KEY = "your_google_maps_api_key"
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run main.py
    ```

2. Open your browser and go to `http://localhost:8501` to interact with the application.

## Project Structure


