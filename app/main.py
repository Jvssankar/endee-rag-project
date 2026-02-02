from fastapi import FastAPI
from app.rag import ask_question

app = FastAPI()

@app.get("/ask")
def ask(q: str):
    return ask_question(q)
