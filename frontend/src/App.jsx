import { useState } from 'react'

function App() {
  const [analysis, setAnalysis] = useState(""); // stores ai response
  const [loading, setLoading] = useState(false); // tracks if Ai is working 
  // users click button -> start the ai process 
  const runAgent = async () => {
    setLoading(true); // start loading ai is working
    try { // try api request
      // Ask our Python server for data!
      const response = await fetch("http://127.0.0.1:8000/api/analyze");
      // convert response to json
      const data = await response.json();
      
      // Save ai answer on memory to display 
      setAnalysis(data.analysis);
    } catch (error) { // if api request fails
      console.error("Error asking the AI:", error); // show message 
      setAnalysis("Error: Make sure your Python server is running!");
    } 
    setLoading(false); // stop loading
  };

  return (
    <div style={{ padding: "40px", fontFamily: "sans-serif" }}>
      <h1>AutoInsight Agent</h1>
      <p>Automated Customer Feedback Analysis</p>
      
      
      <button 
        onClick={runAgent} // when clicked run the ai function 
        disabled={loading} // disable button while ai is working 
        style={{ marginTop:"20px", padding: "10px 20px", fontSize: "16px", cursor: "pointer" }}
      >
        {loading ? "AI is analyzing..." : "Run Analysis"} 
        {/* if loading show this text else show this text */}
      </button>

      {analysis && (
        <div style={{ marginTop: "30px", padding: "10px", backgroundColor: "#f4f4f5", borderRadius: "8px" }}>
          <pre style={{ whiteSpace: "pre-wrap", fontFamily: "inherit" }}>
            {analysis}
          </pre>
        </div>
      )}
    </div>
  )
}

export default App
