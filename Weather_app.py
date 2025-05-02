import streamlit as st
import requests

st.markdown(
    """
  <style>
    .stApp{
        background-image : url("https://i.pinimg.com/736x/64/c6/5c/64c65c607ffc49a62e3b523a6b92838b.jpg");
        background-attachment : fixed;
        background-size : cover;
    }    

   </style>                    
     """,
unsafe_allow_html=True
)

def get_weather(city):
    api_key = "71b702ed4f74f756e22a0b80b5cba3d0"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    city = data["name"]
    country = data["sys"]["country"]
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    speed = data['wind']['speed']
    return city, country, temp, description, humidity, pressure, speed

st.title("🌦️ Weather APP")
city = st.text_input("Enter city")

if city:
    try:
        city, country, temp, description, humidity, pressure, speed = get_weather(city)
        st.success(f"Weather in {city}, {country}")
        st.write(f"🌡️ Temperature: {temp} °C")
        st.write(f"☁️ Description: {description.title()}")
        st.write(f"💧 Humidity: {humidity}%")
        st.write(f"🧭 Pressure: {pressure} hPa")
        st.write(f"🌬️ Wind Speed: {speed} m/s")
    except Exception as e:
        st.error(f"Something went wrong: {e}")
