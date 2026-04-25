from google import genai
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")

st.title("Comparacion entre Gemini 3 Flash y Gemma 4 Ollama")
client = genai.Client()

pregunta = st.text_area(
    "Escribe tu pregunta para Gemini",
    value="Explain how AI works, response in Spanish, in a poetic way, with a maximum of 100 words.",
)

if st.button("Consultar Gemini"):
    if not pregunta.strip():
        st.warning("Por favor escribe una pregunta antes de consultar.")
    else:
        with st.spinner("Consultando Gemini..."):
            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=pregunta,
            )
        st.write("Gemini 3 Flash:")
        st.write(response.text)