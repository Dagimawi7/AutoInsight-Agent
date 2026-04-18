from fastapi import FastAPI
from openai import OpenAI
from backend.tools import get_complaints
from backend.prompts import SYSTEM_PROMPT

# Automatically pull your OPENAI_API_KEY from your system environment variables
client = OpenAI()

# Initialize the server
app = FastAPI()

@app.get("/api/analyze")
def run_agent():
    # 1. Grab our fake data from tools.py
    complaints = get_complaints()

    # 2. Ask the LLM to analyze it
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Here are the complaints: {complaints}"}
        ]
    )

    result_text = response.choices[0].message.content
    
    # 3. Return the result back to whoever asked (frontend)
    return {"status": "success", "analysis": result_text}
