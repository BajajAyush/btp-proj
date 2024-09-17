import React from "react";
import { Link } from "react-router-dom";
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to the Optimization App</h1>
        <p>Click below to input parameters:</p>
        <Link to="/parameters">Input Parameters</Link>
        <p>Click below to calculate the results:</p>
        <Link to="/calculate">Calculate Results</Link>
        <p>Click below to input third parameters:</p>
        <Link to="/thirdparameters">Input Third Parameters</Link>
      </header>
    </div>
  );
}

export default App;
