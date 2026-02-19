from src.chunking.tokenizer import E5Tokenizer
from src.config import CHUNK_SIZE, CHUNK_OVERLAP

tokenizer = E5Tokenizer()

def chunk_text_by_tokens(text: str):
    words = text.split()
    chunks = []

    current_chunk = []
    current_tokens = 0

    for word in words:
        current_chunk.append(word)
        current_tokens = tokenizer.count_tokens(" ".join(current_chunk))

        if current_tokens >= CHUNK_SIZE:
            chunk_text = " ".join(current_chunk)
            chunks.append(chunk_text)

            # overlap logic
            overlap_words = current_chunk[-CHUNK_OVERLAP:]
            current_chunk = overlap_words
            current_tokens = tokenizer.count_tokens(" ".join(current_chunk))

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
