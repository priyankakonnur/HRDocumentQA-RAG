# HR Policy RAG Assistant

A Retrieval-Augmented Generation (RAG) application built using:

- Python
- Ollama
- Qdrant
- LangChain Text Splitter
- PDF document ingestion

This project allows users to ask questions from HR policy documents using semantic search and local LLMs.

---

# Features

- PDF document ingestion
- Text preprocessing
- Intelligent chunking
- Embedding generation using Ollama
- Vector storage using Qdrant
- Semantic similarity search
- Context-aware question answering
- Fully local RAG pipeline

---

# Project Architecture

```text
                ┌────────────────────┐
                │   HR Policy PDF    │
                └─────────┬──────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ PDF Extraction  │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Preprocessing   │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Text Chunking   │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Ollama Embedding│
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │     Qdrant      │
                 │   Vector Store  │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Semantic Search │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Local LLM Answer│
                 └─────────────────┘
```

---

# Project Structure

```text
RAG/
│
├── ingestion.py
├── retrieval.py
├── config.yaml
│
├── utils/
│   ├── loader.py
│   ├── preprocessing.py
│   ├── chunking.py
│   ├── embedding.py
│   └── vectorstore.py
│
├── data/
│   └── hr_policy_detailed_5_pages.pdf
│
├── requirements.txt
└── README.md
```

---

# Technologies Used

- Python
- Ollama
- Qdrant
- LangChain
- PyPDF
- Requests

---

# Installation

## 1. Clone the Repository

```bash
git clone <your-repository-url>
cd RAG
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Install Ollama

Download and install Ollama:

https://ollama.com

---

# Pull Required Models

## Embedding Model

```bash
ollama pull nomic-embed-text
```

## LLM Model

```bash
ollama pull llama3
```

---

# Start Ollama

```bash
ollama serve
```

---

# Start Qdrant

## Using Docker

```bash
docker run -p 6333:6333 qdrant/qdrant
```

---

# Configuration

Create a `config.yaml` file:

```yaml
ollama:
  embedding_model: nomic-embed-text
  llm_model: llama3

qdrant:
  host: localhost
  port: 6333
  collection_name: hr_policy
  vector_size: 768
```

---

# Add PDF Document

Place your PDF inside the project folder.

Example:

```text
data/hr_policy_detailed_5_pages.pdf
```

Update the path in `ingestion.py`:

```python
PDF_PATH = r"data/hr_policy_detailed_5_pages.pdf"
```

---

# Run Document Ingestion

```bash
python ingestion.py
```

Expected Output:

```text
Loading PDF...
Preprocessing...
Chunking...
Generating embeddings via Ollama...
Connecting Qdrant...
Ingesting vectors...
✅ Ingestion completed
```

---

# Run Question Answering

```bash
python retrieval.py
```

Example:

```text
Ask a question:
What is the leave policy?
```

---

# Example Workflow

## User Question

```text
What are the company working hours?
```

## Retrieval Process

- Query converted into embeddings
- Similar chunks retrieved from Qdrant
- Context sent to local LLM

## Generated Answer

```text
The standard company working hours are from 9 AM to 6 PM.
```

---

# Utility Modules

## `loader.py`

Responsible for:
- Reading PDF documents
- Extracting text page by page

---

## `preprocessing.py`

Responsible for:
- Removing extra spaces
- Cleaning text
- Normalizing content

---

## `chunking.py`

Responsible for:
- Splitting large text into smaller chunks
- Applying overlap for better retrieval

---

## `embedding.py`

Responsible for:
- Generating embeddings using Ollama API

---

## `vectorstore.py`

Responsible for:
- Creating Qdrant collections
- Inserting vectors into Qdrant

---

# Recommended Improvements

- Add metadata filtering
- Add source citations
- Add conversational memory
- Implement reranking
- Hybrid search (BM25 + Vector Search)
- FastAPI deployment
- Streamlit UI
- Async embedding generation
- Multi-document support

---

# Common Errors

## Ollama Connection Error

Ensure Ollama is running:

```bash
ollama serve
```

---

## Qdrant Connection Error

Ensure Qdrant container is running:

```bash
docker ps
```

---

## Embedding Dimension Mismatch

Make sure:

```yaml
vector_size: 768
```

matches the embedding model dimensions.

---

# Sample requirements.txt

```text
qdrant-client
pypdf
requests
pyyaml
langchain-text-splitters
```

---

# Future Enhancements

- Web interface
- Chat history memory
- Agentic RAG
- Multi-PDF ingestion
- Citation generation
- Evaluation metrics
- GPU acceleration

---


# Author

Developed as a Generative AI RAG project using Ollama and Qdrant.