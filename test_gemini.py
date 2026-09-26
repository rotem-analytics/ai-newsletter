# Quick test: send one prompt to Gemini and print the reply.

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()  # reads GEMINI_API_KEY from .env

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents="In one sentence, what is a weekly newsletter?",
)

print(response.text)
