# Endee RAG Assignment – AI Document Question Answering System

## Project Overview
This project demonstrates a Retrieval Augmented Generation (RAG)
pipeline using Endee as a high-performance vector database.
The system enables semantic search over documents by storing
and retrieving embeddings using vector similarity.

## Problem Statement
Large Language Models often hallucinate when responding without
relevant context. This project addresses the issue by retrieving
semantically relevant documents using vector search before
producing responses.

## System Architecture
1. Documents are converted into embeddings using a sentence transformer
2. Embeddings are stored inside Endee vector database
3. User queries are embedded and searched in Endee
4. Top matching documents are returned as contextual information

## Technology Stack
- Python
- FastAPI
- Sentence Transformers
- Endee Vector Database
- Docker

## How Endee Is Used
Endee acts as the vector storage and similarity search engine.
Document embeddings are stored via Endee REST APIs, and semantic
similarity search is performed during query time.

## Data Ingestion
The ingestion pipeline reads documents, generates embeddings,
and stores them inside Endee. The output of ingestion is persisted
within the vector database and validated through retrieval queries.

## API Endpoint
GET /ask?q=What is Endee?

## Use Cases
- Semantic Search
- Retrieval Augmented Generation (RAG)
- AI Knowledge Assistants

## Notes
This project focuses on correct system design, integration with
Endee, and clear explanation of vector-based retrieval workflows.

## Author
B.Tech 2026 – Endee.io Campus Assignment
