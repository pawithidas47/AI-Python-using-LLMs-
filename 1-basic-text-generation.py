import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = "เขียนสโลแกนสั้นๆ ที่สะดุดหูสำหรับร้านกาแฟที่เป็นมิตรกับสิ่งแวดล้อมแห่งใหม่"
print(f"Sending prompt: '{prompt}'")
response = client.models.generate_content(
    model='gemini-2.0-flash-lite', # Fast, cheap model for text generation
    contents=prompt
)
print("\nResponse:")
print(response.text)