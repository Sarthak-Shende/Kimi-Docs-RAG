import os
from dotenv import load_dotenv
from google import genai
from src.config import GENERATION_MODEL
from src.generation.prompts import build_grounded_prompt

load_dotenv()


class GeminiGenerator:
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    def generate_answer(self, query: str, retrieved_docs):
        prompt = build_grounded_prompt(query, retrieved_docs)

        response = self.client.models.generate_content(
            model=GENERATION_MODEL,
            contents=prompt
        )

        return response.text
