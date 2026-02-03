import os
import requests
from embeddings import generate_embedding

ENDEE_URL = "http://localhost:8080"
INDEX_NAME = "default"

def ingest_documents():
    docs_dir = "../data/docs"

    for filename in os.listdir(docs_dir):
        file_path = os.path.join(docs_dir, filename)

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        vector = generate_embedding(content)

        payload = {
            "id": filename,
            "vector": vector,
            "metadata": {
                "text": content
            }
        }

        requests.post(
            f"{ENDEE_URL}/api/v1/index/{INDEX_NAME}/upsert",
            json=payload
        )

if __name__ == "__main__":
    ingest_documents()
