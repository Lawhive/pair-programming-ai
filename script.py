
import openai
import os
from dotenv import load_dotenv

load_dotenv('.env', override=True)

openai.api_key = os.environ.get("OPENAI_API_KEY")

response = openai.chat.completions.create(
    model="gpt-4-0125-preview",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful and proactive AI lawyer named Lawrence working with your client."
        },
        {
            "role": "user",
            "content": "Tell me the meaning of life in 20 words or less."
        }
    ],
    temperature=0,
)

print(response.choices)