from fastapi import FastAPI
import os
from openai import OpenAI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "NamEx Backend is running 🚀"}

@app.get("/test-openai")
def test_openai():
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return {"error": "OPENAI_API_KEY not found"}

        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": "Say hello to NamEx."}
            ]
        )

        return {"response": response.choices[0].message.content}

    except Exception as e:
        return {"error": str(e)}
