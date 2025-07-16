import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = """
What do you think could be a good name for a flower shop 
that specializes in selling bouquets of dried flowers more 
than fresh flowers?
"""

response = client.models.generate_content(
  model='gemini-2.5-flash',
  contents=prompt,
  config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_budget=0)
  )
)

print("\nResponse:")
print(response.text)