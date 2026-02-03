
## Overview

EndeeRAG is a Retrieval Augmented Generation (RAG) based project that demonstrates
how a vector database (Endee) can be used to enable semantic document search and
question answering. Instead of relying on keyword matching, the system retrieves
relevant information based on semantic similarity using vector embeddings.

This project is developed as part of the Endee.io campus assignment and focuses on
clear system design, correct usage of Endee, and conceptual understanding of
vector-based retrieval systems.

---

## Problem Statement

Traditional keyword-based search systems fail to capture the semantic meaning of
text. Similarly, Large Language Models may hallucinate when responding without
relevant context.

This project solves these issues by:
- Converting documents into semantic embeddings
- Storing embeddings in a vector database (Endee)
- Retrieving the most relevant documents using similarity search
- Using retrieved context for question answering

---

## What is Retrieval Augmented Generation (RAG)?

Retrieval Augmented Generation (RAG) is an AI architecture where:
1. Relevant information is retrieved from a knowledge base
2. The retrieved context is used to augment the response generation

In this project:
- Retrieval is handled by Endee
- Augmentation is done by returning relevant document text

---

## System Architecture

Documents  
↓  
Embedding Model  
↓  
Endee Vector Database  
↓  
Similarity Search  
↓  
Relevant Context  
↓  
User Response  

---

## Technology Stack

- Python
- FastAPI
- Sentence Transformers
- Endee Vector Database
- Docker

---

## Project Structure

```

EndeeRAG/
│
├── backend/
│   ├── app.py
│   ├── embeddings.py
│   ├── ingest.py
│   └── query.py
│
├── data/
│   └── docs/
│       └── sample.txt
│
├── docker-compose.yml
├── requirements.txt
└── README.md

```

---

## Data Ingestion Pipeline

The ingestion pipeline is responsible for loading documents into Endee.

Steps performed during ingestion:
1. Documents are read from the data/docs directory
2. Each document is converted into a vector embedding
3. Embeddings are stored inside Endee along with metadata

The ingestion script does not produce visible console output. Its output is
persisted inside the Endee vector database and validated later through semantic
search queries. This behavior reflects real-world production data pipelines.

---

## Semantic Search Workflow

When a user submits a query:
1. The query is converted into an embedding
2. Endee performs vector similarity search
3. The top matching documents are retrieved
4. Relevant document content is returned

This approach enables meaning-based retrieval rather than keyword matching.

---

## API Endpoint

```

GET /ask?q=<your question>

```

Example:
```

GET /ask?q=What is Endee?

```

---

## How Endee Is Used

Endee acts as the core vector database in this project.

Responsibilities of Endee:
- Store high-dimensional embedding vectors
- Perform fast similarity search
- Return relevant vectors for a given query

The project interacts with Endee purely through REST APIs, treating it as a
production-ready vector storage system.

---

## Scalability

Although this demo uses a small document set, the architecture can scale to:
- Large document collections
- Enterprise knowledge bases
- Full-scale RAG systems

Scalability strategies include document chunking, batch ingestion, and bulk
vector operations.

---

## Use Cases

- Semantic Search
- Document Question Answering
- AI Knowledge Assistants
- Retrieval Augmented Generation (RAG)
- Vector-based Search Systems

---

## Validation Strategy

Instead of printing embeddings, correctness is validated by:
- Executing semantic search queries
- Verifying the relevance of retrieved documents

This aligns with standard practices in AI system development.

---

## Assignment Relevance

This project satisfies all assignment requirements:
- Uses Endee as the vector database
- Demonstrates a practical AI use case
- Implements semantic search and RAG concepts
- Includes clean project structure and documentation

---

## Author

B.Tech 2026  
Endee.io Campus Assignment  

---

## One-Line Summary

EndeeRAG is a Retrieval Augmented Generation system that uses Endee as a vector
database to enable semantic document search and question answering.


