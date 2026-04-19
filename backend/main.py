from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google import genai
from dotenv import load_dotenv
import os
from backend.tools import get_complaints
from backend.prompts import SYSTEM_PROMPT

# load secret key 
load_dotenv() 

# get the key and set up Gemini
client = genai.Client()

# Initialize the server 
app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Allow fronted access
    allow_credentials=True,
    allow_methods=["*"], # Allow all types of requests
    allow_headers=["*"],
)

# Test if server is running 
@app.get("/")
def read_root():
    return {"message": "Welcome to the AutoInsight Agent API"} 

# run the ai agent when the frontend clicks the button 
@app.get("/api/analyze")
def run_agent():
    # Grab our dummy data from tools.py
    complaints = get_complaints()
    # create the prompt for the ai agent 
    prompt_text = f"{SYSTEM_PROMPT}\n\nHere are the complaints:\n{complaints}"
    
    # call gemini to analyze the data 
    response = client.models.generate_content( 
        model="gemini-3-flash-preview", # the model we are using 
        contents=prompt_text,
    )
    return {"status": "success", "analysis": response.text} # return the response to the frontend 