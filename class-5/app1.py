import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("No se encontro OPENAI_API_KEY en el archivo .env")
    st.stop()

st.title("Comparacion entre OpenAI y Gemma 4 Ollama")
client = OpenAI(api_key=api_key)

pregunta = st.text_area(
    "Escribe tu pregunta para OpenAI",
    value="Explain how AI works, response in Spanish, in a poetic way, with a maximum of 100 words.",
)

if st.button("Consultar OpenAI"):
    if not pregunta.strip():
        st.warning("Por favor escribe una pregunta antes de consultar.")
    else:
        with st.spinner("Consultando OpenAI..."):
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=pregunta,
            )
        st.write("OpenAI GPT-4.1-mini:")
        st.write(response.output_text)
