import os
from langchain_community.vectorstores import Chroma
from src.config import EMBEDDING_MODEL, VECTOR_STORE_DIR
from src.ingestion.gemini_embeddings import GeminiEmbeddingFunction


def build_chroma_index(documents):
    embedding_function = GeminiEmbeddingFunction(
        model_name=EMBEDDING_MODEL
    )

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embedding_function,
        persist_directory=VECTOR_STORE_DIR
    )

    vector_store.persist()

    return vector_store
