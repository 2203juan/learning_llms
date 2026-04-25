import os
from dotenv import load_dotenv
from openai import OpenAI


def is_true(value: str | None) -> bool:
    return (value or "").strip().lower() in {"1", "true", "yes", "on"}


def main() -> None:
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "No se encontro OPENAI_API_KEY. Crea un archivo .env basado en .env.example"
        )

    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    use_web_search = is_true(os.getenv("OPENAI_USE_WEB_SEARCH", "false"))
    client = OpenAI(api_key=api_key)

    messages = [
        {
            "role": "system",
            "content": "Eres un asistente util, breve y claro.",
        }
    ]

    print(f"Modelo: {model}")
    print(f"Web search: {'activado' if use_web_search else 'desactivado'}")
    print("Escribe tu mensaje. Usa 'salir' para terminar.\n")

    while True:
        user_text = input("Tu: ").strip()
        if user_text.lower() in {"salir", "exit", "quit"}:
            print("Fin de la conversacion.")
            break

        messages.append({"role": "user", "content": user_text})

        try:
            if use_web_search:
                response = client.responses.create(
                    model=model,
                    input=messages,
                    tools=[{"type": "web_search_preview"}],
                )
            else:
                response = client.responses.create(
                    model=model,
                    input=messages,
                )
            assistant_text = response.output_text.strip()
        except Exception as exc:
            print(f"Error llamando a OpenAI: {exc}")
            continue

        print(f"Asistente: {assistant_text}\n")
        messages.append({"role": "assistant", "content": assistant_text})


if __name__ == "__main__":
    main()
