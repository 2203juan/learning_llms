# Learning LLMs: from local models to tool-using agents

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![uv](https://img.shields.io/badge/uv-DE5FE9?style=flat-square&logo=uv&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)

Hands-on exercises from my **M.Sc. in Artificial Intelligence & Data Science** (Universidad Autónoma de Occidente). Each class builds one step up: from calling a local model, to provider APIs, to comparing providers, to an agent that calls tools.

## What's inside

| Folder | What it does | Key pieces |
|---|---|---|
| [`class-3`](class-3) | CLI that streams responses from a **local model** | Ollama, `argparse`, streaming |
| [`class-4/openai-chat-base`](class-4/openai-chat-base) | Base chat project against the **OpenAI API**, configured by environment variables | OpenAI SDK, `.env` config |
| [`class-5`](class-5) | Four Streamlit apps (see below) | Streamlit, OpenAI, Gemini, LangChain |

### class-5 apps

| Command | App |
|---|---|
| `make openai` | Chat UI on OpenAI |
| `make gemini` | Chat UI on Google Gemini |
| `make comparar` | **Gemini vs OpenAI** side by side, with optional web-search grounding on each provider |
| `make langchain` | **LangChain agent** with a `get_weather` tool (geocoding + live weather API) |

## Run it

Every project uses [uv](https://docs.astral.sh/uv/):

```bash
cd class-5
uv sync
# create a .env file with your OpenAI and Gemini API keys
make comparar
```

For `class-3` you need [Ollama](https://ollama.com) running locally with a model pulled.

## Author

**Juan José Hoyos Urcué** · [Website](https://2203juan.github.io/my-site/) · [LinkedIn](https://www.linkedin.com/in/hoyosjuan)
