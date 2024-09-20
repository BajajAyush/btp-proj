import React from "react";
import { Link } from "react-router-dom";
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to the Welding Optimization App</h1>
        <p> Optimum Procedure for Parameters specified by User</p>
        <Link to="/parameters">Input Parameters</Link>
        <p>Optimum Procedure for Default Parameter Ranges</p>
        <Link to="/calculate">Calculate Results</Link>
        <p>Optimum Procedure for specified Response, Penetration</p>
        <Link to="/thirdparameters">Calculate Results</Link>
      </header>
    </div>
  );
}

export default App;
