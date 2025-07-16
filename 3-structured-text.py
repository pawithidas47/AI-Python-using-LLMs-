import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

structured_prompt = [
    types.Content(
        role="user",
        parts=[
            types.Part.from_text(text="เขียนสโลแกนสั้นๆ ที่สะดุดหูสำหรับร้านกาแฟที่เป็นมิตรกับสิ่งแวดล้อมแห่งใหม่")
        ]
    )
]
print(f"Sending structured prompt: {structured_prompt}")
response = client.models.generate_content(
    model='gemini-2.0-flash-lite',
    contents=structured_prompt,
    config=types.GenerateContentConfig(response_mime_type="text/plain")
)
print("\nResponse:")
print(response.text)