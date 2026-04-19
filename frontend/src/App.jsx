import { useState } from 'react';
import './App.css';

function App() {
  const [analysis, setAnalysis] = useState(null); 
  const [loading, setLoading] = useState(false); 

  const runAgent = async () => {
    setLoading(true);
    setAnalysis(null);
    try { 
      const response = await fetch("http://127.0.0.1:8000/api/analyze");
      const data = await response.json();
      setAnalysis(data.analysis); 
    } catch (error) { 
      console.error(error);
    } 
    setLoading(false); 
  };

  return (
    <div className="dashboard">
      <div className="header-row">
        <h1>AI Customer Feedback Agent</h1>
        <button 
          className="btn-primary"
          onClick={runAgent} 
          disabled={loading} 
        >
          {loading ? "Agent Processing Data..." : "Run AI Analysis"} 
        </button>
      </div>

      {analysis && !loading && (
        <>
          <div className="glass-card summary-card">
            <p style={{ color: "#9ca3af", fontWeight: "600", fontSize: "14px", marginBottom: "8px" }}>EXECUTIVE SUMMARY (LAST 30 DAYS)</p>
            <p style={{ fontSize: "18px", color: "#fff", lineHeight: "1.6", margin: 0 }}>
              {analysis.summary}
            </p>
          </div>

          <div className="bento-grid">
            
            {/* The Left Column: Red Issues */}
            <div>
              <div className="column-title">Top 3 Critical Issues</div>
              <ul>
                {analysis.problems.map((prob, index) => (
                  <li key={index} className="glass-card issue-card">
                    <span className="badge-red">CRITICAL</span>
                    <p style={{ margin: 0 }}>{prob}</p>
                  </li>
                ))}
              </ul>
            </div>

            {/* The Right Column: Green Actions */}
            <div>
              <div className="column-title">Recommended Action Plan</div>
              <ul>
                {analysis.solutions.map((sol, index) => (
                  <li key={index} className="glass-card action-card">
                    <span className="badge-green">TO-DO</span>
                    <p style={{ margin: 0 }}>{sol}</p>
                  </li>
                ))}
              </ul>
            </div>

          </div>
        </>
      )}
    </div>
  )
}

export default App;
