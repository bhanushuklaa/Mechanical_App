import React from 'react';

function Login() {
  return (
    <div className="p-8 max-w-md mx-auto mt-10 border border-gray-300 shadow-md rounded-md">
      <h2 className="text-2xl font-semibold mb-4">Login</h2>
      <input type="email" placeholder="Email" className="w-full mb-4 p-2 border" />
      <button className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Login</button>
    </div>
  );
}

export default Login;
