import requests

OLLAMA_URL = "http://localhost:11434/api/embeddings"    #all the embedding models stored in this link by default

def generate_embeddings(chunks, model):

    vectors = []

    for chunk in chunks:

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": model,
                "prompt": chunk
            }
        )

        data = response.json()

        if "embedding" not in data:
            print("Ollama response error:", data)
            raise Exception("Embedding not returned")

        vectors.append(data["embedding"])

    return vectors

#Embedding model = nomic-embed-text    
#1. Integrity – We act with honesty and transparency in all professional dealings, 0.324
#2. Ownership – Employees are encouraged to take responsibility beyond assigned tasks.

