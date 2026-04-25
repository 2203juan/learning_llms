from langchain.agents import create_agent
import dotenv
import streamlit as st

dotenv.load_dotenv()

st.title("LangChain Agent Example")
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="openai:gpt-5.4",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
st.write(result["messages"][-1].content_blocks)