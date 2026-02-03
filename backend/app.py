from fastapi import FastAPI
from query import search

app = FastAPI(title="Endee RAG Assignment")

@app.get("/ask")
def ask_question(q: str):
    return search(q)
