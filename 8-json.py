import json
import os
from google import genai
from google.genai import types
from pydantic import BaseModel

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class Recipe(BaseModel):
    recipe_name: str
    recipe_description: str
    recipe_ingredients: list[str]

response = client.models.generate_content(
    model='gemini-2.0-flash-lite',
    contents="Provide a popular som tam recipe and its ingredients.",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=Recipe,
    ),
)

print(json.dumps(json.loads(response.text), indent=4))