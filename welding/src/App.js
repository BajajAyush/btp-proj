import React from "react";
import Header from "./components/Header";
import Card from "./components/Card"; 
import './App.css';

function App() {
  return (
    <div className="App">
      <Header />
      <header className="App-header">
        <Card 
          title="Input Parameters" 
          description="Optimum Procedure for Parameters specified by User" 
          to="/parameters" 
        />
        <Card 
          title="Calculate Results" 
          description="Optimum Procedure for Default Parameter Ranges" 
          to="/calculate" 
        />
        <Card 
          title="Penetration Calculation" 
          description="Optimum Procedure for specified Response, Penetration" 
          to="/thirdparameters" 
        />
      </header>
    </div>
  );
}

export default App;
