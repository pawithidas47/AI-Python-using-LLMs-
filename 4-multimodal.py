import os
from google import genai
from PIL import Image

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

image = Image.open("banded_krait.jpg")
image.thumbnail([512,512])

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[
        image,
        "เขียนคำอธิบายสั้นๆ ของภาพนี้ ซึ่งเหมาะสำหรับเป็นสารคดีสัตว์ป่าเพื่อการศึกษาสำหรับเด็กอายุต่ำกว่า 10 ปี รวมถึงชื่อของสัตว์ ถิ่นที่อยู่อาศัย และข้อเท็จจริงสนุกๆ เกี่ยวกับสัตว์นั้นๆ"
    ]
)
print("\nResponse:")
print(response.text)