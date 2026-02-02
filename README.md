# ENDEE RAG PROJECT

## Project Overview & Problem Statement

Large Language Models (LLMs) are powerful, but they lack access to your private or custom documents. This project solves that problem using **Retrieval-Augmented Generation (RAG)**.
The system allows users to:
- Store documents in a vector database  
- Search them semantically  
- Ask questions in natural language  
- Receive AI-generated answers grounded in their own data  
This prevents hallucinations and ensures answers come from **your documents**, not just general model knowledge.

---

## System Design / Technical Approach

The system follows a **Retrieval-Augmented Generation (RAG)** pipeline:
1. **Document Ingestion**
   - Text documents are split into smaller chunks
   - Each chunk is converted into a numerical embedding
2. **Vector Storage**
   - Embeddings are stored in **Endee Vector Database**
3. **User Question Flow**
   - User asks a question via API
   - Question is converted into an embedding
   - Endee performs similarity search
   - Top matching document chunks are retrieved
4. **Answer Generation**
   - Retrieved context + user question are sent to the LLM
   - The LLM generates a grounded answer
---

## How Endee is Used in This Project
**Endee** acts as the **vector database** for storing and searching document embeddings.
It is used for:
- Storing document chunk embeddings  
- Performing similarity search for user queries  
- Returning the most relevant document pieces for answer generation  
### Endee Workflow in This System
- Document → Embedding → Stored in Endee
- User Question → Embedding → Search in Endee → Retrieve Context
- Context + Question → LLM → Final Answer

Without Endee, the system would not be able to perform fast semantic search over documents.

---

# STEP-BY-STEP SETUP GUIDE

Follow these steps from scratch to run the project.

---

## STEP 1 — Clone the Repository
```bash
git clone <your-github-repo-url>
cd endee-rag-project
```

## STEP 2 — Create Virtual Environment
Windows
```bash
python -m venv venv
venv\Scripts\activate
```

## STEP 3 - Install Required Packages
```bash
pip install -r requirements.txt
```

## STEP 4 - Create .env File
In the project root, create a file named:
```bash
.env
```
Add the following inside:
```bash
ENDEE_URL=http://localhost:8000
COLLECTION_NAME=my_docs
```

## STEP 5 — Start Endee Vector Database

If running locally using Docker:
```bash
docker run -p 8000:8000 endee/vector-db
```
Make sure Endee is accessible before continuing. You should be able to open Endee in your browser.

## STEP 6 - Ingest Sample Document into Endee
A sample file is already provided:
```bash
data/sample_docs.txt
```
Add the following inside:
```bash
python -m app.ingest
```
This step:
- Reads the sample document
- Splits it into chunks
- Converts chunks to embeddings
- Stores them as vectors in Endee

or

How to Use Your Own Documents
You can replace the contents of:
```bash
data/sample_docs.txt
```
with your own text data and run:
```bash
python -m app.ingest
```
If you want to ingest PDFs or other formats, modify ingest.py accordingly.

## STEP 7 — Start the FastAPI Server
```bash
uvicorn app.main:app --reload
```
Server runs at:
```bash
http://127.0.0.1:8001
```

## STEP 8 — Ask Questions
Open in browser:
```bash
http://127.0.0.1:8001/docs
```
Use the /ask endpoint.
Example question:
```bash
What is discussed in the document?
```

System flow:
- Your question → embedding
- Search Endee for top matching document chunks
- Send context + question to LLM
- Return AI-generated answer
