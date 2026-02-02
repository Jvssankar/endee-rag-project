from sentence_transformers import SentenceTransformer, util
from app.llm import generate_answer

model = SentenceTransformer("all-MiniLM-L6-v2")

# 🔹 Your documents (same ones you inserted into Endee)
documents = [
    "RAG stands for Retrieval-Augmented Generation.",
    "It combines vector search with large language models.",
    "Embeddings are used to find similar documents."
]

# Precompute document embeddings once
doc_embeddings = model.encode(documents, convert_to_tensor=True)

def ask_question(question: str):
    # Embed question
    query_embedding = model.encode(question, convert_to_tensor=True)

    # Compute similarity
    scores = util.cos_sim(query_embedding, doc_embeddings)[0]

    # Get top 2 documents
    top_results = scores.topk(k=2)

    context = [documents[i] for i in top_results.indices]

    answer = generate_answer(question, context)

    return {
        "question": question,
        "context": context,
        "answer": answer
    }
