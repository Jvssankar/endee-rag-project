from app.endee_client import add_vector
from app.embeddings import embed

def ingest():
    with open("data/sample_docs.txt", "r", encoding="utf-8") as f:
        docs = [line.strip() for line in f if line.strip()]

    for i, doc in enumerate(docs):
        vector = embed(doc)

        add_vector(
            id=f"doc_{i}",
            vector=vector,
            metadata={"text": doc}
        )

        print(f"Inserted doc_{i}")

    print("✅ Ingestion completed")

if __name__ == "__main__":
    ingest()
