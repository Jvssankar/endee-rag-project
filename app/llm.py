from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

def generate_answer(question: str, context: list[str]) -> str:
    if not context:
        return "I don't know based on the provided documents."

    context_text = "\n".join(context)

    prompt = f"""
Answer the question using ONLY the context below.
If the answer is not in the context, say "I don't know".

Context:
{context_text}

Question:
{question}

Answer:
"""

    output = generator(
        prompt,
        max_length=200,
        do_sample=True,
        temperature=0.7
    )

    return output[0]["generated_text"].split("Answer:")[-1].strip()
