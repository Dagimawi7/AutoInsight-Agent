# AutoInsight Agent

A full-stack, AI-powered system that automates the analysis of customer feedback by extracting insights, identifying critical issues, and generating structured execution plans using Chain of Thought reasoning.

## 🎯 Problem Statement

Many customer success and product teams spend hours manually reviewing raw customer feedback, complaints, and support tickets. This process is repetitive, deeply time-consuming, and prone to human error, which delays engineering responses to critical bugs and limits strategic decision-making. 

## 💡 Solution

I built an AI-powered workflow automation agent that:
- Accepts raw text data (customer complaints)
- Deeply processes the data using a multi-step Chain of Thought approach
- Uses Gemini LLMs to synthesize summaries, extract patterns, and format solutions
- Outputs the results natively into an Enterprise-grade React Dashboard with visual priority tagging

The system reduces analysis time from hours to seconds and enables proactive decision-making.

## ⚙️ How It Works 

Our agent utilizes a "Multi-Step" autonomous workflow rather than simple prompting:

1. **Input Layer:** Fetches raw unstructured data (from JSON/CSV mock data) 
2. **Synthesis Strategy:** Uses Gemini to synthesize a concise, high-level executive summary
3. **Extraction Strategy:** Takes the summary and asks the LLM to recursively extract the top 3 critical issues
4. **Action Strategy:** Takes the extracted issues and asks the LLM to design an immediate action plan for the engineering team
5. **Output Layer:** Structures the results into JSON objects and maps them to a responsive React Grid Layout

## 🧩 Architecture

- **Backend:** Python (FastAPI)
- **AI Model:** Google Gemini (`gemini-3-flash-preview` via `google-genai` SDK)
- **Frontend:** React + Vite
- **Styling:** Vanilla CSS (Glassmorphism, CSS Grid)

**Flow:**
Raw Data → FastAPI Orchestrator → Multi-Step Gemini API → Structured JSON → React Bento-Box Dashboard

## 🚀 Features

- **Chain of Thought Reasoning:** Breaks complex analysis into smaller, high-accuracy steps
- **Negative Prompting:** Explicitly prevents markdown hallucinations
- **Responsive Dashboard:** Glowing, glassmorphic UI with dynamic Red (Critical) and Green (To-Do) badges
- **Modular Pipeline:** System instructions, tools, and endpoints are completely decoupled

## 📊 Example Output

**Input:** 
*Raw JSON feed of customer complaints describing app crashes and billing errors.*

**Output:**
```json
{
  "summary": "Customers are experiencing significant mobile app crashes and checkout billing errors.",
  "problems": [
    "Mobile app frequently crashes on launch",
    "Billing gateway fails during checkout"
  ],
  "solutions": [
    "Deploy hotfix v2.1.1 immediately",
    "Implement retry logic for the payment API"
  ]
}
```

## 🧠 AI Design Decisions

- **Chain of Thought Sequencing:** Instead of one massive prompt, the backend creates an execution pipeline of three sequential LLM calls, feeding the result of the previous call into the next context window. This dramatically improved output logic and quality.
- **Strict Format Bounding:** Used negative prompting ("DO NOT use Markdown formatting") inside the system instructions to force the LLM to return sanitizable plain text, ensuring clean JSON serialization.
- **Decoupled Architecture:** Built `tools.py` and `prompts.py` so the foundational logic can easily map to a real Database or alternate models (OpenAI, Claude) without modifying the FastAPI routing.

## 🔧 Future Improvements

- Add agent-based task chaining (allowing the agent to automatically push the "To-Do" list to a Jira board)
- Integrate webhooks to automatically trigger analysis when new Zendesk tickets arrive
- Implement memory vectors to track complaint trends across multiple months

## ▶️ How to Run

1. **Clone the repo:** `git clone https://github.com/Dagimawi7/AutoInsight-Agent.git`
2. **Environment Setup:** Create a `.env` file in the root and add `GEMINI_API_KEY=your_key_here`
3. **Start the Backend:** 
   ```bash
   uvicorn backend.main:app --reload
   ```
4. **Start the Frontend:**
   ```bash
   cd frontend
   npm run dev
   ```
5. Open your browser to `http://localhost:5173`
