import requests
from embeddings import generate_embedding

ENDEE_URL = "http://localhost:8080"
INDEX_NAME = "default"

def search(query: str, top_k: int = 3):
    vector = generate_embedding(query)

    payload = {
        "vector": vector,
        "top_k": top_k
    }

    response = requests.post(
        f"{ENDEE_URL}/api/v1/index/{INDEX_NAME}/search",
        json=payload
    )

    return response.json()
