import streamlit as st
import requests

import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env



# Apply custom CSS with a working background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1503264116251-35a269479413?auto=format&fit=crop&w=1600&q=80");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        font-family: 'Segoe UI', sans-serif;
    }

    .glass-box {
        background: rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 2rem;
        margin-top: 2rem;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        color: white;
    }

    input, label {
        color: black !important;
    }

    h1, h3, p, strong {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# App title
st.markdown("<h1 style='text-align: center;'>☁️ Weather App ⚡</h1>", unsafe_allow_html=True)

# Input
city = st.text_input("📍 Enter city name", placeholder="e.g., Paris")

# Weather data fetching function
def get_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temp": data['main']['temp'],
            "description": data['weather'][0]['description'].title(),
            "humidity": data['main']['humidity'],
            "pressure": data['main']['pressure'],
            "speed": data['wind']['speed']
        }
    else:
        raise Exception("City not found or API error.")
    


# Weather display
if city:
    with st.spinner("Fetching weather..."):
        try:
            weather = get_weather(city)
            st.markdown('<div class="glass-box">', unsafe_allow_html=True)
            st.markdown(f"""
                <h3 style='text-align: center;'>🌍 {weather["city"]}, {weather["country"]}</h3>
                <p><strong>🌡️ Temperature:</strong> {weather["temp"]} °C</p>
                <p><strong>☁️ Condition:</strong> {weather["description"]}</p>
                <p><strong>💧 Humidity:</strong> {weather["humidity"]}%</p>
                <p><strong>🔽 Pressure:</strong> {weather["pressure"]} hPa</p>
                <p><strong>🌬️ Wind Speed:</strong> {weather["speed"]} m/s</p>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"❌ Error: {e}")
