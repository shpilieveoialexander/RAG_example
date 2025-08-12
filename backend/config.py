import os


class Settings:
    FAISS_INDEX_FILE = os.getenv("FAISS_INDEX_FILE", "faiss_index.pkl")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    if OPENAI_API_KEY is None:
        raise RuntimeError(
            "Set OPENAI_API_KEY environment variable to use this example"
        )


settings = Settings()
