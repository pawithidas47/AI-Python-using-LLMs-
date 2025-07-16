import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = """
   How can you obtain 565 with 25 8 3 7 and 1?
   You can only use a number once.
   You can use addition, subtraction, multiplication, and division.
   If you cannot obtain the number, find the closest number you can obtain with the given numbers.
   Output the mathematical expression and what it equals.
   Do not include any words or explanation.
   Example output: (25 * 3) + 8 = 83
"""

response = client.models.generate_content(
  model='gemini-2.5-flash',
  contents=prompt,
  config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
      thinking_budget=0,
      include_thoughts=True
    )
  )
)

for part in response.candidates[0].content.parts:
  if not part.text:
    continue
  if part.thought:
    print("Thought summary:")
    print(part.text)
    print()
  else:
    print("Answer:")
    print(part.text)
    print()