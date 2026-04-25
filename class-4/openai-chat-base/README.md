# Proyecto base: chat con OpenAI (Python)

## 1) Instalar uv (si no lo tienes)

```powershell
winget install --id=astral-sh.uv -e
```

## 2) Crear entorno virtual

```powershell
uv venv
.\.venv\Scripts\Activate.ps1
```

## 3) Instalar dependencias

```powershell
uv sync
```

## 4) Configurar API key

1. Copia `.env.example` a `.env`
2. Coloca tu clave en `OPENAI_API_KEY`

Ejemplo:

```env
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4.1-mini
OPENAI_USE_WEB_SEARCH=true
```

`OPENAI_USE_WEB_SEARCH` puede ser `true/false`.

## 5) Ejecutar

```powershell
uv run python src/chat.py
```

Para salir del chat, escribe `salir`.

Si `OPENAI_USE_WEB_SEARCH=true`, el asistente puede consultar la web en tiempo real usando la tool nativa de OpenAI.

## Comandos utiles con uv

```powershell
uv add requests
uv lock
```

