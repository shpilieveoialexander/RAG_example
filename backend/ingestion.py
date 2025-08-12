from fastapi import File, Form, UploadFile
from langchain.text_splitter import RecursiveCharacterTextSplitter

from db import embeddings, load_vectorstore, save_vectorstore

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)


async def ingest_text(text: str = None, file: UploadFile = None):
    if not text and not file:
        return 0

    if file:
        contents = await file.read()
        try:
            text = contents.decode("utf-8")
        except Exception:
            text = str(contents)

    docs = splitter.split_text(text)

    vectorstore = load_vectorstore()
    if vectorstore is None:
        from langchain.vectorstores import FAISS

        vectorstore = FAISS.from_texts(docs, embeddings)
    else:
        vectorstore.add_texts(docs)

    save_vectorstore(vectorstore)

    return len(docs)
