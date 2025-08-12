# RAG FastAPI Example

This project is a complete **Retrieval-Augmented Generation (RAG)** API built with **FastAPI** and **LangChain**.  
It allows you to ingest documents into a vector store and query them using a Large Language Model (LLM) for context-aware answers.

---

## 🚀 Features
- **FastAPI Backend** – High-performance, production-ready web API.
- **Document Ingestion** – Upload plain text or files (`.txt`, `.pdf`) into a vector database.
- **RAG Querying** – Combine document retrieval with LLM generation for accurate, context-rich answers.
- **OpenAPI Docs** – Interactive API documentation via Swagger UI and ReDoc.
- **LangChain Integration** – Built using the latest, non-deprecated LangChain methods.

---

## 📌 Endpoints
| Method | Endpoint   | Description |
|--------|-----------|-------------|
| POST   | `/ingest` | Upload and process documents to build the knowledge base |
| POST   | `/query`  | Ask questions and receive answers enriched by your documents |
| GET    | `/health` | Check API operational status |

---

## 🛠 Prerequisites
- Python **3.9+** (if running locally)
- `pip` (Python package installer)
- **Docker & Docker Compose** (if running via container)

---

## 📦 Installation (Local)

1. **Clone the repository**
   ```bash
   git clone git@github.com:shpilieveoialexander/RAG_example.git
