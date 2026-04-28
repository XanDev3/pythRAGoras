import chromadb

client = chromadb.PersistentClient(path="./db")
collection = client.get_or_create_collection("docs")

with open("london-to-seattle-miles.txt", "r") as f:
    text = f.read()

collection.add(documents=[text], ids=["londonToSeattle"])

print("Embedding 'London to Seattle' stored in Chroma")

with open("k8s.txt", "r") as f:
    text = f.read()

collection.add(documents=[text], ids=["k8s"])

print("Embedding 'k8s' stored in Chroma")