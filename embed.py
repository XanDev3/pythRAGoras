import chromadb

client = chromadb.PersistentClient(path="./db")
collection = client.get_or_create_collection("docs")

with open("london-to-seattle-miles.txt", "r") as f:
    text = f.read()

collection.add(documents=[text], ids=["londonToSeattle"])

print("Embedding stored in Chroma")
