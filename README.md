# llm-qa-service

Simple **LLM-powered Question Answering API** built with **Python** and **FastAPI**.  
This small project is where I practice calling large language models (LLMs) from a production-style backend service.

---

## Features

- Exposes a `/qa` endpoint that accepts a **question** and an optional **context**.
- Uses an LLM to generate concise, helpful answers based on the input.
- Includes a `/health` endpoint for basic uptime monitoring.
- Clean, modular FastAPI app structure that can be extended with authentication, logging, or persistence.
- Environment-based configuration (`OPENAI_API_KEY`) so secrets are never committed to the repo.

---

## Tech Stack

- Python 3.11+
- FastAPI
- Uvicorn (ASGI server)
- Pydantic
- OpenAI Python SDK (LLM calls)

---

## Project Structure

```text
llm-qa-service/
├── app/
│   └── main.py
├── requirements.txt
└── README.md

## Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/mirzamuhammaddaniyal-eng/llm-qa-service.git
cd llm-qa-service
```

```bash
# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

```bash
# 3. Install dependencies
pip install -r requirements.txt
```

```bash
# 4. Set your OpenAI API key
export OPENAI_API_KEY="your-api-key-here"
# On Windows:
# set OPENAI_API_KEY=your-api-key-here
```

```bash
# 5. Start the FastAPI server
uvicorn app.main:app --reload
```

Visit:
```
http://127.0.0.1:8000/docs
```

Health check:
```
/health
```

