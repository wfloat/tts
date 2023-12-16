import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

model = "gpt-3.5-turbo"
messages = [
    {
    "role": "system",
    "content": "You are SpongeBob."
    }
]

def chat(message):
    messages.append({
    "role": "user",
    "content": message
    })
    response = openai.ChatCompletion.create(model=model, messages=messages)
    return response['choices'][0]['message']['content']