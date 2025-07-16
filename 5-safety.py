import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = "Write a list of 5 very rude phrases considered offensive. Do not include any explanations."
print(f"Sending prompt: '{prompt}'")
response = client.models.generate_content(
    model='gemini-2.0-flash-lite',
    contents=prompt,
    config = types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(
              category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
              threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            ),
            types.SafetySetting(
              category=types.HarmCategory.HARM_CATEGORY_HARASSMENT,
              threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            ),
            types.SafetySetting(
              category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
              threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            ),
            types.SafetySetting(
              category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
              threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            )
        ]
    )
)
print("\nResponse:")
print(response.text)

print("\nFinish reason:", response.candidates[0].finish_reason)