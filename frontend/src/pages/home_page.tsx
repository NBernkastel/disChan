import React from 'react';
import { Link } from 'react-router-dom';

const Home_page: React.FC = () => {
  return (
    <div className="bg-dark text-white d-flex flex-column align-items-center justify-content-center" style={{ minHeight: '1vh' }}>
      <h1 style={{ fontSize: '30px' }}>Welcome to the DisChan</h1>
      <div className="mt-3">
        <Link to="/Sign Up" className="btn btn-primary mr-2">
          Sign Up
        </Link>
        <Link to="/Sign In" className="btn btn-secondary">
          Sign In
        </Link>
      </div>
      <div className="mt-3">
        <p style={{ fontSize: '20px' }}>This is a sample text block. 😊</p>
      </div>
    </div>
  );
}

export default Home_page;