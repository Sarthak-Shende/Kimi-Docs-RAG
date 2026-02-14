import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Fix: Change 'gemini-3-flash' to 'gemini-3-flash-preview'
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What are the important parts of RAG"
)

print(response)