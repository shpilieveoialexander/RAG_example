from typing import List, Optional

from pydantic import BaseModel


class IngestResponse(BaseModel):
    added_chunks: int


class QueryRequest(BaseModel):
    query: str
    top_k: Optional[int] = 4


class QueryResponse(BaseModel):
    answer: str
    sources: List[str]
