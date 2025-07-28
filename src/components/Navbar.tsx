import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav className="flex justify-between items-center p-4 bg-gradient-to-r from-orange-500 via-white to-green-500 text-black">
      <Link to="/" className="text-xl font-bold">
        🇮🇳 Mechanical Store
      </Link>
      <div className="space-x-4">
          <Link to="/home" className="font-semibold hover:underline">Home</Link>
          <Link to="/login" className="font-semibold hover:underline">Login</Link>
          <Link to="/signup" className="font-semibold hover:underline">Signup</Link>
          <Link to="/services" className="font-semibold hover:underline">Services</Link>
      </div>
    </nav>
  );
}

export default Navbar;
