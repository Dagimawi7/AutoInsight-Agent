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
    summary_resp = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=f"Summarize these customer complaints into exactly two short sentences. Keep it plain text: {complaints}"
    )
    summary = summary_resp.text
    # takes summary and takes out the main problems 
    patterns_resp = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=f"Read this summary and list the top 3 specific problems. Output ONLY the problems on new lines starting with a dash (-). Plain text only: {summary}"
    )
    patterns = patterns_resp.text
    # takes problems and comes up with solutions 
    solutions_resp = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=f"Read these problems and provide 3 immediate actions the company should take to fix them. Output ONLY the actions on new lines starting with a dash (-). Plain text only: {patterns}"
    )
    solutions = solutions_resp.text
    # gives the final report 
    structured_report = f"QUICK SUMMARY\n{summary}\n\nTOP 3 PROBLEMS\n{patterns}\n\nCOMPANY ACTION PLAN\n{solutions}"
    
    return {"status": "success", "analysis": structured_report}