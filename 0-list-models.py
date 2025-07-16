import os
import sys
from google import genai

# Read API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("Error: GEMINI_API_KEY environment variable not set.")
    print("Please set it in your environment or .env file.")
    sys.exit(1)

# Instantiate the genai client
client = genai.Client(api_key=GEMINI_API_KEY)

# List models
print("Available Models:")
for model in client.models.list():
    print(f"  - {model.name}")
