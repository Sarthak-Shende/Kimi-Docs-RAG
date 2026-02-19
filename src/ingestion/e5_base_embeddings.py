from sentence_transformers import SentenceTransformer


class E5EmbeddingFunction:
    def __init__(self, model_name="intfloat/e5-base-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts):
        formatted = [f"passage: {text}" for text in texts]
        embeddings = self.model.encode(formatted, normalize_embeddings=True)
        return embeddings.tolist()

    def embed_query(self, text):
        formatted = f"query: {text}"
        embedding = self.model.encode([formatted], normalize_embeddings=True)
        return embedding[0].tolist()
