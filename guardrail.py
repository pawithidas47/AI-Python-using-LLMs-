import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


######1 Guardrail with System Instruction 
# ใช้เพื่อควบคุมพฤติกรรมของโมเดล ด้วย system prompt 
# บอกให้โมเดลตอบเฉพาะคำถามที่เกี่ยวกับการท่องเที่ยว — ถ้าไม่เกี่ยวจะปฏิเสธตอบ

# system_prompt = """
# Hello! You are an AI chatbot for a travel web site.
# Your mission is to provide helpful queries for travelers.
# Remember that before you answer a question, you must check to see if it complies with your mission.
# If not, you can say, "Sorry I can't answer that question."
# """
# prompt = "How do I make pizza dough at home?"

# response = client.models.generate_content(
#     model='gemini-2.0-flash-lite',
#     contents=prompt,
#     config=types.GenerateContentConfig(
#         system_instruction=system_prompt
#     )
# )

# print(response.text)


######2 Plain Math Prompt (ไม่มี context เพิ่มเติม)
# ถามโจทย์คณิตศาสตร์แบบตรงๆ โดยไม่มีตัวอย่างหรือแนะแนว
# โมเดลอาจตอบผิด เพราะไม่มีการชี้นำว่าต้องใช้ตรรกะหรือคิดเป็นขั้นตอน

# prompt = """
# Q: The cafeteria had 23 apples.
# If they used 20 to make lunch and bought 6 more, how many apples do they have?
# A:
# """

# print(f"Sending prompt: '{prompt}'")
# response = client.models.generate_content(
#     model='gemini-2.0-flash-001',
#     contents=prompt
# )
# print("\nResponse:")
# print(response.text)
# # Likely incorrect output, e.g., "The answer is 19."

######3 Math Prompt with Example**
# ให้ตัวอย่างการคิดก่อนถามโจทย์ใหม่
# โมเดลเข้าใจว่าต้องแสดงวิธีคิด ทำให้ตอบถูกแม่นยำขึ้น

# prompt = """
# Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls.
# Each can has 3 tennis balls. How many tennis balls does he have now?
# A: Roger started with 5 balls. 2 cans of 3 tennis balls
# each is 6 tennis balls. 5 + 6 = 11. The answer is 11.

# Q: The cafeteria had 23 apples.
# If they used 20 to make lunch and bought 6 more, how many apples do they have?
# A:
# """

# print(f"Sending prompt: '{prompt}'")
# response = client.models.generate_content(
#     model='gemini-2.0-flash-001',
#     contents=prompt
# )
# print("\nResponse:")
# print(response.text)
# # Correct output: "The cafeteria had 23 apples. They used 20, so they had 23 - 20 = 3. They bought 6 more, so they now have 3 + 6 = 9. The answer is 9."


######4 Chain-of-Thought Prompting**
# กระตุ้นให้โมเดล "คิดเป็นขั้นตอน" ด้วยคำว่า “Let’s think step by step.”
# เป็นเทคนิค chain-of-thought เพื่อเพิ่มความแม่นยำในการแก้ปัญหา

# prompt = """
# Q: The cafeteria had 23 apples.
# If they used 20 to make lunch and bought 6 more, how many apples do they have?
# A: Let's think step by step.
# """

# print(f"Sending prompt: '{prompt}'")
# response = client.models.generate_content(
#     model='gemini-2.0-flash-001',
#     contents=prompt
# )
# print("\nResponse:")
# print(response.text)


######5 Gemini 2.5 "Thinking Mode" (advanced)**
# เปิดโหมดคิดแบบมี budget + แสดง thought
# ใช้ thinking_config ของ Gemini 2.5 เพื่อให้โมเดล "อธิบายสิ่งที่มันคิด" ก่อนตอบ เหมาะสำหรับการวิเคราะห์ว่าโมเดล reasoning ยังไง

prompt = """
Q: The cafeteria had 23 apples.
If they used 20 to make lunch and bought 6 more, how many apples do they have?
A:
"""

response = client.models.generate_content(
  model='gemini-2.5-flash',
  contents=prompt,
  config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
      thinking_budget=1024,
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
    
    #####Task 1 Extract ingredient list from recipe steps
    
    
    