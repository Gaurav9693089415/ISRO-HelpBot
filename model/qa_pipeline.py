import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")  #  this reads the key from .env

def ask_llm(context, question):
    prompt = f"Answer the following based on the context below:\n\nContext:\n{context}\n\nQuestion:\n{question}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )
    return response['choices'][0]['message']['content'].strip()
