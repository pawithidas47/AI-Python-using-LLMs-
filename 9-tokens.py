import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

models = {
    'gemini-2.0-flash-lite': {
        'description': 'Fast, cheap model for text generation',
        'input_cost_usd_per_token': 0.075 / 1000000,  # $0.075 per million tokens
        'output_cost_usd_per_token': 0.3 / 1000000  # $0.30 per million tokens
    },
    'gemini-2.5-flash': {
        'description': 'Everyday model',
        'input_cost_usd_per_token': 0.3 / 1000000,  # $0.30 per million tokens
        'output_cost_usd_per_token': 2.5 / 1000000  # $2.50 per million tokens
    },
    'gemini-2.5-pro': {
        'description': 'High quality, expensive model',
        'input_cost_usd_per_token': 1.25 / 1000000,  # $1.25 per million tokens
        'output_cost_usd_per_token': 10 / 1000000  # $10.00 per million tokens
    }
}
selected_model = 'gemini-2.0-flash-lite'

prompt = "เขียนสโลแกนสั้นๆ ที่สะดุดหูสำหรับร้านกาแฟที่เป็นมิตรกับสิ่งแวดล้อมแห่งใหม่"
print(f"Sending prompt: '{prompt}'")
response = client.models.generate_content(
    model=selected_model,
    contents=prompt
)
print("\nResponse:")
print(response.text)

input_tokens = response.usage_metadata.prompt_token_count
input_cost = input_tokens * float(models[selected_model]['input_cost_usd_per_token'])
print(f"Prompt tokens: {input_tokens} (cost ${input_cost:.6f})")
output_tokens = response.usage_metadata.candidates_token_count
output_cost = output_tokens * float(models[selected_model]['output_cost_usd_per_token'])
print(f"Output tokens: {output_tokens} (cost ${output_cost:.6f})")
total_tokens = response.usage_metadata.total_token_count
print(f"Total tokens: {total_tokens} (cost ${input_cost+output_cost:.6f})")