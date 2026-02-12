import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def count_tokens(text: str) -> int:
  result = client.models.count_tokens(
    model="gemini-3-flash-preview",
    contents=text
  )
  return result.total_tokens

def chunk_text_by_tokens(
    text: str,
    max_tokens: int = 1500,
    overlap_tokens: int = 150
):
    words = text.split()
    chunks = []

    current_chunk = []
    current_tokens = 0

    for word in words:
        current_chunk.append(word)
        current_tokens = count_tokens(" ".join(current_chunk))

        if current_tokens >= max_tokens:
            chunk_text = " ".join(current_chunk)
            chunks.append(chunk_text)

            # overlap
            overlap_words = current_chunk[-overlap_tokens:]
            current_chunk = overlap_words
            current_tokens = count_tokens(" ".join(current_chunk))

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
