import argparse
from ollama import chat

def stream_response(model: str, prompt: str, system: str | None, temperature: float, max_tokens: int | None):
    messages = []
    if system:
        messages.append({'role': 'system', 'content': system})
    messages.append({'role': 'user', 'content': prompt})

    options = {'temperature': temperature}
    if max_tokens:
        options['num_predict'] = max_tokens

    print(f"\n[modelo: {model} | temp: {temperature}] Generando", end="", flush=True)

    stream = chat(model=model, messages=messages, stream=True, options=options)

    print(" ▶\n")
    for chunk in stream:
        token = chunk['message']['content']
        print(token, end="", flush=True)

    print("\n\n[listo]")

def main():
    parser = argparse.ArgumentParser(description="Chat con Ollama desde la terminal")
    parser.add_argument("prompt", nargs="?", default="Why is the sky blue?", help="Mensaje al modelo")
    parser.add_argument("--model", "-m", default="qwen3.6", help="Modelo a usar (default: qwen3.6)")
    parser.add_argument("--system", "-s", default=None, help="System prompt")
    parser.add_argument("--temperature", "-t", type=float, default=0.7, help="Temperatura 0.0–2.0 (default: 0.7)")
    parser.add_argument("--max-tokens", "-n", type=int, default=None, help="Máximo de tokens a generar")

    args = parser.parse_args()
    stream_response(args.model, args.prompt, args.system, args.temperature, args.max_tokens)

if __name__ == "__main__":
    main()
