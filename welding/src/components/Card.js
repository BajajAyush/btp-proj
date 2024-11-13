import React from 'react';
import { Link } from 'react-router-dom';
import './Card.css';

function Card({ title, description, to }) {
  return (
    <Link to={to} className="Card">
      <h3>{title}</h3>
      <p>{description}</p>
    </Link>
  );
}

export default Card;
