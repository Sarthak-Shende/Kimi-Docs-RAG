from sentence_transformers import SentenceTransformer


class E5Tokenizer:
    def __init__(self, model_name="intfloat/e5-base-v2"):
        self.model = SentenceTransformer(model_name)
        self.tokenizer = self.model.tokenizer

    def count_tokens(self, text: str) -> int:
        # Count tokens using e5 tokenizer
        tokens = self.tokenizer(
            text,
            truncation=False,
            return_tensors=None
        )
        return len(tokens["input_ids"])
