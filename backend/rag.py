from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document

from config import settings
from db import embeddings, load_vectorstore


def query_rag(query: str, top_k: int = 4):
    vectorstore = load_vectorstore()
    if vectorstore is None:
        return "No documents ingested.", []

    retriever = vectorstore.as_retriever(k=top_k)

    llm = ChatOpenAI(openai_api_key=settings.OPENAI_API_KEY, temperature=0.0)

    prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:
    <context>
    {context}
    </context>
    Question: {input}""")

    document_chain = create_stuff_documents_chain(llm, prompt)

    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    result = retrieval_chain.invoke({"input": query})
    answer = result["answer"]

    # Use retriever.invoke(query) instead of the deprecated method
    docs: list[Document] = retriever.invoke(query)
    sources = [d.metadata.get("source", "uploaded") for d in docs]

    return answer, sources