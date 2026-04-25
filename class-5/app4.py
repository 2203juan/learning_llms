from langchain.agents import create_agent
import dotenv
import streamlit as st
import requests
from datetime import datetime
from geopy.geocoders import Nominatim

dotenv.load_dotenv()

st.title("LangChain Agent Example")

def get_weather(city: str) -> str:
    """Get weather for a given city with temperature in Celsius."""
    try:
        # Obtener coordenadas de la ciudad
        geolocator = Nominatim(user_agent="weather_app")
        location = geolocator.geocode(city)

        if not location:
            return f"No se pudo encontrar la ciudad: {city}"

        # API de Open-Meteo (gratuita, sin autenticación)
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": location.latitude,
            "longitude": location.longitude,
            "current": "temperature_2m,weather_code",
            "timezone": "auto"
        }

        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # Extraer información del clima
        current = data["current"]
        temp = current["temperature_2m"]
        timezone = data["timezone"]

        # Obtener hora y fecha actual en la zona horaria de la ciudad
        now = datetime.now()
        fecha_hora = now.strftime("%A, %d de %B de %Y - %H:%M")

        return f"Ciudad: {city}\nTemperatura: {temp}°C\nFecha: {fecha_hora}\nZona horaria: {timezone}"

    except Exception as e:
        return f"Error al obtener el clima: {str(e)}"

agent = create_agent(
    model="openai:gpt-5.4",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)
message = st.chat_input("Cual es el clima en Madrid?")
result = agent.invoke(
    {"messages": [{"role": "user", "content": message}]}
)
st.write(result["messages"][-1].content_blocks[0]["text"])