import React from 'react';

function Home() {
  return (
    <div className="text-center py-20">
      <h1 className="text-5xl font-bold text-orange-500">Welcome to Mechanical Store</h1>
      <div className="my-8">
        <img
          src="https://upload.wikimedia.org/wikipedia/commons/1/17/Ashoka_Chakra.svg"
          alt="Ashoka Chakra"
          className="mx-auto w-32 animate-spin-slow"
        />
      </div>
      <p className="text-lg text-gray-600">Doorstep bike and car services at your convenience</p>
    </div>
  );
}

export default Home;
