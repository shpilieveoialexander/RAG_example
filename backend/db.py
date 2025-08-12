import os

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from config import settings

embeddings = OpenAIEmbeddings(
    model=settings.EMBEDDING_MODEL,
    openai_api_key=settings.OPENAI_API_KEY,
)


def load_vectorstore():
    if os.path.exists(settings.FAISS_INDEX_FILE):
        try:
            return FAISS.load_local(
                settings.FAISS_INDEX_FILE,
                embeddings,
                allow_dangerous_deserialization=True,
            )
        except Exception as e:
            print("Failed to load FAISS index, creating new one:", e)
    return None


def save_vectorstore(vectorstore):
    vectorstore.save_local(settings.FAISS_INDEX_FILE)
