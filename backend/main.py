import uvicorn
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.openapi.utils import get_openapi

from db import load_vectorstore
from ingestion import ingest_text
from rag import query_rag
from schemas import IngestResponse, QueryRequest, QueryResponse

app = FastAPI(
    title="RAG FastAPI Example",
    description=(
        "🚀 **Retrieval-Augmented Generation API**\n\n"
        "Allows you to ingest documents into a FAISS vector database and perform "
        "retrieval-augmented generation queries using an LLM (OpenAI).\n\n"
        "**Endpoints:**\n"
        "- `/ingest` — upload text or a file to the vector store\n"
        "- `/query` — run a RAG query\n"
        "- `/health` — check API health\n\n"
        "📄 *Swagger and ReDoc are available automatically*"
    ),
    version="1.0.0",
    contact={
        "name": "Alex Shpilievoi",
        "email": "shpilevoy29@gmail.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)


@app.post("/ingest", response_model=IngestResponse, tags=["Ingestion"])
async def ingest_endpoint(
    text: str = Form(None, description="Plain text to ingest"),
    file: UploadFile = File(None, description="File to ingest (txt, pdf, etc.)"),
):
    """
    Ingest plain text or a file into the FAISS vector store.

    - **text**: optional plain text
    - **file**: optional file (e.g., .txt or .pdf)
    """
    chunks_added = await ingest_text(text, file)
    return IngestResponse(added_chunks=chunks_added)


@app.post("/query", response_model=QueryResponse, tags=["Query"])
async def query_endpoint(payload: QueryRequest):
    """
    Perform a RAG query against the vector store.

    - **query**: question to ask
    - **top_k**: number of most relevant documents to retrieve
    """
    answer, sources = query_rag(payload.query, payload.top_k)
    return QueryResponse(answer=answer, sources=sources)


@app.get("/health", tags=["System"])
async def health():
    """Check API health and whether a vector index exists."""
    return {"status": "ok", "has_index": load_vectorstore() is not None}


# Custom OpenAPI schema
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
        contact=app.contact,
        license_info=app.license_info,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=80,
        log_level="info",
        reload=True,
    )
