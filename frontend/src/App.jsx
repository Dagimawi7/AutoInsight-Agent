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
    <div className="art-canvas">
      {/* Background Fluid Light System */}
      <div className="ambient-light light-cyan"></div>
      <div className="ambient-light light-magenta"></div>
      <div className="ambient-light light-violet"></div>

      <div className="interface-container">
        
        <header className="art-header">
          <h1 className="art-title">Noctra</h1>
          <div className="art-subtitle">AutoInsight Agent</div>
        </header>

        <button 
          className="core-activator"
          onClick={runAgent} 
          disabled={loading} 
        >
          {loading ? <span className="loading-pulse">Awakening...</span> : "Run Analysis"} 
        </button>

        {analysis && !loading && (
          <div className="data-constellation">
            
            <div className="glass-shard summary-block stagger-1">
              <div className="shard-title">Summary</div>
              <p className="summary-text">
                {analysis.summary}
              </p>
            </div>

            <div className="glass-shard issue-block stagger-2">
              <div className="shard-title">Top 3 Problems</div>
              <ul className="abstract-list">
                {analysis.problems.map((prob, index) => (
                  <li key={index}>{prob}</li>
                ))}
              </ul>
            </div>

            <div className="glass-shard action-block stagger-3">
              <div className="shard-title">Recommended Actions</div>
              <ul className="abstract-list">
                {analysis.solutions.map((sol, index) => (
                  <li key={index}>{sol}</li>
                ))}
              </ul>
            </div>

          </div>
        )}
      </div>
    </div>
  )
}

export default App;
