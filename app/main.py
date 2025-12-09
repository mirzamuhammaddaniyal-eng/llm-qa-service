from fastapi import FastAPI
import os
from pydantic import BaseModel

app = FastAPI(title="LLM QA Service")

class Question(BaseModel):
    question: str
    context: str | None = None

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/qa")
def answer_question(payload: Question):
    # Dummy response so repo looks valid
    answer = f"You asked: '{payload.question}'. This is a mock answer."
    return {"answer": answer}
