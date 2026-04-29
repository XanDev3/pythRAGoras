import chromadb
from chromadb.utils.embedding_functions.ollama_embedding_function import (
    OllamaEmbeddingFunction,
)

client = chromadb.PersistentClient(path="./chroma_db")

ef = OllamaEmbeddingFunction(
    model_name="nomic-embed-text",
    url="http://localhost:11434",
)

collection = client.get_or_create_collection(
    name="personal_profile",
    embedding_function=ef,
)

with open("london-to-seattle-miles.txt", "r") as f:
    text = f.read()

collection.add(documents=[text], ids=["londonToSeattle"])

print("Embedding 'London to Seattle' stored in Chroma")

with open("k8s.txt", "r") as f:
    text = f.read()

collection.add(documents=[text], ids=["k8s"])

print("Embedding 'k8s' stored in Chroma")