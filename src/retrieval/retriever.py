from langchain_chroma import Chroma
from src.ingestion.e5_base_embeddings import E5EmbeddingFunction
from src.config import EMBEDDING_MODEL, VECTOR_STORE_DIR


def load_vector_store():
    embedding_function = E5EmbeddingFunction(model_name=EMBEDDING_MODEL)

    vector_store = Chroma(
        persist_directory=VECTOR_STORE_DIR,
        embedding_function=embedding_function
    )

    return vector_store


def retrieve(query: str, k: int = 3):
    vector_store = load_vector_store()

    # Step 1: retrieve more than needed
    initial_k = 6
    results = vector_store.similarity_search(query, k=initial_k)

    query_lower = query.lower()

    def score(doc):
        base_score = 1  # all retrieved are already similar

        section_title = doc.metadata.get("section_title", "").lower()

        boost = 0
        for word in query_lower.split():
            if word in section_title:
                boost += 1

        return base_score + boost

    # Step 2: rerank
    reranked = sorted(results, key=score, reverse=True)

    # Step 3: return top-k
    return reranked[:k]

