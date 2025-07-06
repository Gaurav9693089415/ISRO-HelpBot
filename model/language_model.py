import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_llm(context: str, question: str) -> str:
    prompt = f"""Use the following context to answer the user's question.
    
Context:
{context}

Question:
{question}

Answer:"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "system", "content": "You are a helpful assistant trained on ISRO and MOSDAC knowledge."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4,
            max_tokens=400,
        )
        return response.choices[0].message["content"].strip()
    
    except Exception as e:
        return f" LLM Error: {e}"
