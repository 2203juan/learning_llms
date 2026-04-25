import os

import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types
from openai import OpenAI

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")


os.environ["GEMINI_API_KEY"] = gemini_api_key

openai_client = OpenAI(api_key=openai_api_key)
gemini_client = genai.Client()

st.title("Comparador Gemini vs OpenAI")
st.caption("Una pregunta, dos respuestas lado a lado.")

openai_models = [
    "gpt-4.1-mini",
    "gpt-4.1-nano",
    "gpt-4.1",
    "gpt-4o-mini",
    "o4-mini",
    "o3-mini",
]

gemini_models = [
    "gemini-2.5-flash-lite",
    "gemini-2.5-flash",
    "gemini-2.0-flash-lite",
    "gemini-2.0-flash",
]

st.sidebar.header("Configuracion de modelos")
selected_openai_model = st.sidebar.selectbox("Modelo OpenAI", openai_models)
selected_gemini_model = st.sidebar.selectbox("Modelo Gemini", gemini_models)
use_web_search = st.sidebar.checkbox("Activar busqueda web", value=True)

pregunta = st.text_area(
    "Escribe tu pregunta",
    value="Explain how AI works, response in Spanish, in a poetic way, with a maximum of 100 words.",
)

if st.button("Comparar modelos"):
    if not pregunta.strip():
        st.warning("Por favor escribe una pregunta antes de consultar.")
    else:
        openai_text = None
        gemini_text = None
        openai_error = None
        gemini_error = None

        with st.spinner("Consultando OpenAI y Gemini..."):
            try:
                openai_request = {
                    "model": selected_openai_model,
                    "input": pregunta,
                }
                if use_web_search:
                    openai_request["tools"] = [{"type": "web_search_preview"}]

                openai_response = openai_client.responses.create(**openai_request)
                openai_text = openai_response.output_text
            except Exception as exc:
                openai_error = str(exc)

            try:
                gemini_request = {
                    "model": selected_gemini_model,
                    "contents": pregunta,
                }
                if use_web_search:
                    gemini_request["config"] = types.GenerateContentConfig(
                        tools=[types.Tool(google_search=types.GoogleSearch())]
                    )

                gemini_response = gemini_client.models.generate_content(**gemini_request)
                gemini_text = gemini_response.text
            except Exception as exc:
                gemini_error = str(exc)

        col_openai, col_gemini = st.columns(2)

        with col_openai:
            st.subheader(f"OpenAI {selected_openai_model}")
            if openai_error:
                st.error(f"Error en OpenAI: {openai_error}")
            else:
                st.write(openai_text)

        with col_gemini:
            st.subheader(f"Gemini {selected_gemini_model}")
            if gemini_error:
                st.error(f"Error en Gemini: {gemini_error}")
            else:
                st.write(gemini_text)
