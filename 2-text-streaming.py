import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = "เขียนสโลแกนสั้นๆ ที่สะดุดหูสำหรับร้านกาแฟที่เป็นมิตรกับสิ่งแวดล้อมแห่งใหม่"
print(f"Streaming response for prompt: '{prompt}'")
print("\nResponse:")
for chunk in client.models.generate_content_stream(
    model='gemini-2.5-flash', # Everyday model
    contents=prompt
):
    # Each chunk is a part of the response, print it as it arrives
    print(chunk.text, end="", flush=True) # Use end="" to avoid new lines