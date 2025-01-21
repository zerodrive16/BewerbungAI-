import React, { useEffect } from 'react';

function MainApp({ handleLogin }) {
  useEffect(() => {
    handleLogin(); // Call the login function on mount
  }, [handleLogin]);

  return (
    <div>
      {/* Your app content goes here */}
      <h2>Welcome to My App!</h2>
    </div>
  );
}

export default MainApp;