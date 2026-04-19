from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from dotenv import load_dotenv
import os
from backend.tools import get_complaints
from backend.prompts import SYSTEM_PROMPT

# load secret key 
load_dotenv() 

# Automatically pull your OPENAI_API_KEY from your system environment variables
client = OpenAI()

# Initialize the server 
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Allow fronted access
    allow_credentials=True,
    allow_methods=["*"], # Allow all types of requests
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AutoInsight Agent API"}

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
