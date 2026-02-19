import os
from langchain_community.vectorstores import Chroma
from src.config import VECTOR_STORE_DIR
from src.ingestion.e5_base_embeddings import E5EmbeddingFunction


def build_chroma_index(documents):
    embedding_function = E5EmbeddingFunction()

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embedding_function,
        persist_directory=VECTOR_STORE_DIR
    )

    return vector_store
