import React from 'react';
import { Link } from 'react-router-dom';
import './header.css';

function Header() {
  return (
    <div className="Header">
      <Link to="/" className="Header-link">
        <h1>WeldWell - A Welding Optimization Application</h1>
      </Link>
    </div>
  );
}

export default Header;
